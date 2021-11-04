<template>
  <div>
    <TrainerHeader/>
    <section id="team" class="team section-bg">
      <div class="container" data-aos="fade-up">
        <div class="section-title">
          <!--<div class="createClass">
                  <a href="createClass" class="createClass-btn">Create Class</a>
              </div>-->
          <h2>{{ course.courseName }}</h2>
        </div>
      </div>

      <div class="row">
        <div class="col-lg-6 mt-5" v-for="_class in classes" :key="_class.classId">
          <div
            class="member d-flex align-items-start"
            data-aos="zoom-in"
            data-aos-delay="100"
          >
            <div class="member-info">
              <h4>{{ _class.classTitle }}</h4>
              <span>{{ _class.trainerName }}</span>
              <!-- <p> Maximum Class Capacity: {{_class.classSize}} </p> -->
              <!-- </div> -->
              <!-- <div class="member-info"> -->
              <p> <b> Current Class Size: </b> {{ enrolment[_class.classId] }} / {{_class.classSize}} </p>
              <br>
              <p>
                <b>Enrolment Period: </b> {{_class.enrolmentStartDate}} to {{_class.enrolmentEndDate}}
              </p>
              <br>
              <p>
                <b>Start Date: </b>{{_class.startDate}} 
              </p>
              <p>
                <b>Start Time: </b>{{_class.startTime}} 
              </p>
              <br>
              <p>
                <b>End Date: </b>{{_class.endDate}} 
              </p>
              <p>
                <b>End Time: </b>{{_class.endTime}} 
              </p>
            </div>      
            <div class="viewClass">
              <button class="viewClass-btn" @click="selfEnrol(_class.classId)">Join Class</button>
            </div>
          </div>
        </div>
      </div>
    </section>
  </div>
</template>

<script>
import axios from "axios";

export default {
  data: () => ({
    course: {},
    classes: [],
    error: false,
    message: "",
    enrolment: {},
    courseId: localStorage.getItem('courseId')
  }),
  async mounted() {
    const apiUrl1 = `http://localhost:5002/getClasses/${this.courseId}`;
    const apiUrl2 = `http://localhost:5002/getCourse/${this.courseId}`;
    const getEnrolmentURL = `http://localhost:5004/enrolment/size/${this.courseId}`;
    try {
      let response1 = await axios.get(apiUrl1);
      let response2 = await axios.get(apiUrl2);
      let response3 = await axios.get(getEnrolmentURL);

      this.classes = await response1.data.data;
      this.course = await response2.data;
      this.enrolment = await response3.data.data;

      this.error = false;
    } catch (err) {
      console.log(err);
      this.error = true;
      this.message = err;
    }
  },  
  methods:{
      async selfEnrol(classId){
          const apiUrl = 'http://localhost:5004/enrolLearner';
          const data = {
            classId: classId,
            learnerId: localStorage.getItem('userId')
          }
          try {
            let response = await axios.post(apiUrl, data)
            if (response.status == 201){
              alert("Successfully Enrolled!")
              this.$router.push("/LearnerViewCourseDetails")
            }
            else{
              alert("Please Try Again!")
            }
          }catch(err){
            console.log(err)
          }
      }
  }
};
</script>
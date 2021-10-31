<template>
    <div>
        <TrainerHeader/>
        <section id="team" class="team section-bg">
        <div class="container" data-aos="fade-up">

           <div class="row pb-5 mb-2 ml-0">
            <div class="viewClass">
              <router-link :to="{path: '/TrainerViewClasses', query: {courseId: course.courseId}}" class="viewClass-btn">Back to see all Classes</router-link>
            </div>
          </div>

          <div class="section-title">
              <!--<div class="createClass">
                  <a href="createClass" class="createClass-btn">Create Class</a>
              </div>-->
            <h2>{{classObj.classId}}</h2>
            <h3>{{course.courseName}}</h3>

            <div class="TrainerCreateSection">
                <a href="TrainerCreateSection" class="TrainerCreateSection-btn">Create Section</a>
            </div>
            <div class="TrainerCreateFinalQuiz ">
                <a href="TrainerCreateFinalQuiz" class="TrainerCreateFinalQuiz-btn">Create Final Quiz</a>
            </div>
            
          </div>
              
      
          <div class="row">
            <div class="col-lg-6" v-for="section in sections" :key="section.sectionId">
              <div
                class="member d-flex align-items-start"
                data-aos="zoom-in"
                data-aos-delay="100"
              >
                
                <div class="member-info">
                  <h4>{{section.sectionId}}</h4>
                  <p>
                    Explicabo voluptatem mollitia et repellat qui dolorum quasi
                  </p>
                  
                </div>
                <div class="editSection">  
                    <a href="TrainerCreateSection" class="editSection-btn">Edit Section</a>
                </div>
                

                <div class="quizList">  
                    <a href="TrainerQuizList" class="quizList-btn">Quiz List</a>
                </div>

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
    sections: [],
    classObj: {},
    error: false,
    message: "",
    enrolment: {}
  }),
  async mounted() {
    const apiUrl1 = `http://localhost:5002/viewSections/${this.$route.query.classId}`;
    const apiUrl2 = `http://localhost:5002/getCourse/${this.$route.query.courseId}`;
    const apiUrl3 = `http://localhost:5002/getClass/${this.$route.query.classId}`;
    try {
      let response1 = await axios.get(apiUrl1);
      let response2 = await axios.get(apiUrl2);
      let response3 = await axios.get(apiUrl3);

      console.log(response1)
      console.log(response2)
      console.log(response3)

      this.sections = await response1.data.data;
      this.course = await response2.data;
      this.classObj = await response3.data;
  
      console.log(this.classObj);
      console.log(this.course);
      console.log(this.sections);
      

      this.error = false;
    } catch (err) {
      console.log(err);
      this.error = true;
      this.message = err;
    }
  },

  methods: {
    async viewClassSize(classId){
      const getEnrolmentURL = `http://localhost:5004/enrolment/number/${classId}`;
      try {
        let response = await axios.get(getEnrolmentURL);
  
        console.log(response)
  
        this.enrolment[classId] = response.data.data;
  
        console.log(this.enrolment[classId]);
        console.log(response.data.data);
  
        this.error = false;
      } catch (err) {
        console.log(err);
        this.error = true;
        this.message = err;
      }
    }
  },

};
</script>
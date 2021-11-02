<template>
  <div>
    <Header />
    <section id="team" class="team section-bg">
      <div class="container" data-aos="fade-up">
        <div class="row pb-5 mb-2 ml-0">
          <div class="viewClass">
            <router-link :to="{path: '/ViewCourses'}" class="viewClass-btn">Back to see all Courses</router-link>
          </div>
        </div>
        <div class="section-title">
          <!--<div class="createClass">
                  <a href="createClass" class="createClass-btn">Create Class</a>
              </div>-->
          <h2>{{ course.courseName }}</h2>
          <div class="createClass">
            <router-link  :to="{path: '/CreateClass', query: {courseName: course.courseName}}" class="createClass-btn">Create Class</router-link>
          </div>
        </div>
        
        <div class="row">
          <div class="col-lg-8" id="TrainerViewCourseDetails" style="padding-bottom: 40px">
            <div class="member d-flex align-items-start"
                    data-aos="zoom-in"
                    data-aos-delay="100"
                  >
        
              <div class="member-info">
                <!-- <h4>{{ course.courseName }}</h4> -->
                <h4>Prerequisite Courses:</h4>
                <div v-if="course.prerequisites != ''">
                  <li>{{ course.prerequisites }}</li> <br>
                </div>
                <ul v-else>
                  <li>No prerequisites required</li>
                </ul>
                <h4>Period of Enrollment: </h4> <p>1st July - 30th July</p> <br>
                <h4>Course Description: </h4>
                <p>
                    {{course.courseDescription}}
                </p>
              </div>
            </div>
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
              <p> Current Class Size: {{ enrolment[_class.classId] }} / {{_class.classSize}} </p>
                  <br>
                  <p>
                    Start Date: {{_class.startDate}} 
                  </p>
                  <p>
                    Start Time: {{_class.startTime}} 
                  </p>
                  <br>
                  <p>
                    End Date: {{_class.endDate}} 
                  </p>
                  <p>
                    End Time: {{_class.endTime}} 
                  </p>
            </div>    
              <div class="viewClass">
                <router-link :to="{path: '/EditClass', query: {classId: _class.classId}}" class="viewClass-btn">Edit Class</router-link>
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
    classes: [],
    error: false,
    message: "",
    enrolment: {},
    courseId: localStorage.getItem('courseId')
  }),
  async mounted() {
    const apiUrl1 = `http://localhost:5002/getClasses/${this.courseId}`;
    const apiUrl2 = `http://localhost:5002/getCourse/${this.courseId}`;
    const getEnrolmentURL = `http://localhost:5004/enrolment/size/13/${this.courseId}`;
    try {
      let response1 = await axios.get(apiUrl1);
      let response2 = await axios.get(apiUrl2);
      let response3 = await axios.get(getEnrolmentURL);

      console.log(response1)
      console.log(response2)
      console.log(response3)

      this.classes = await response1.data.data;
      this.course = await response2.data;
      this.enrolment = await response3.data.data;

      console.log(this.classes);
      console.log(this.course)
      console.log(this.enrolment);

      this.error = false;
    } catch (err) {
      console.log(err);
      this.error = true;
      this.message = err;
    }
  },
};
</script>

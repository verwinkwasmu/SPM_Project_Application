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
                
                <h4>Course ID: </h4> 
                <p>{{ course.courseId }}</p> <br>
                <h4>Course Description: </h4>
                          <p>{{course.courseDescription}}</p> <br>
                <h4>Prerequisite Courses:</h4>
                <ul v-if="course.prerequisites != ''">
                  <li>{{ course.prerequisites }}</li> 
                </ul>
                <ul v-else>
                  <li>No prerequisites required</li>
                </ul>
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
                <router-link :to="{path: '/EditClass', query: {classId: _class.classId}}" class="viewClass-btn">Edit Class</router-link>
              </div>
              <div class="approvereject">
                <router-link :to="{path: '/ApproveRejectLearners', query: {classId: _class.classId}}" class="approvereject-btn">Approve/Reject Learners</router-link>
                <!-- routes to ApproveRejectLearners.vue -->
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
    const apiUrl1 = `https://spm-flask.herokuapp.com/getClasses/${this.courseId}`;
    const apiUrl2 = `https://spm-flask.herokuapp.com/getCourse/${this.courseId}`;
    const getEnrolmentURL = `https://spm-flask.herokuapp.com/enrolment/size/${this.courseId}`;
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
};
</script>

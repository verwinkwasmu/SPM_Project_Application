<template>
  <div>
    <LearnerHeader />
    <section id="services" class="services section-bg">
      <div class="container" data-aos="fade-up">
        <div class="section-title">
          <h2>Current Courses</h2>
        </div>
        <div class="row">
          <div
            v-for="course in currentCourses"
            :key="course.courseId"
            class="col-xl-3 col-md-6 d-flex align-items-stretch"
            data-aos="zoom-in"
            data-aos-delay="100"
          >
            <div class="icon-box">
              <div class="icon"><i class="bx bxl-dribbble"></i></div>
              <h4>
                <a href="">{{ course.courseName }}</a>
              </h4>
              <div class="course" v-if="isPastDate(course.enrolmentStartDate,course.enrolmentEndDate)">
                <button disabled
                  class="course-btn"
                  >View Materials</button>
              </div>
              <div class="course" v-else>
                <router-link
                  :to="{
                    path: '/LearnerViewSections',
                    query: {
                      classId: course.classId,
                      courseName: course.courseName,
                      sectionName: 'Section 1'
                    },
                  }"
                  class="btn btn-outline-dark"
                  >View Materials</router-link>
              </div>
            </div>
          </div>
        </div>
         <div style="padding-top: 10px; width: 25.5%;" class="row">
           <div>
           <div  
           v-for="course in currentCourses"
            :key="course.courseId"
            data-aos="zoom-in"
            data-aos-delay="100">

           <b-progress  :max="course.totalNumSections"
                    show-progress
                    animated>
              <b-progress-bar :value="course.sectionsCompleted" :label="`${((course.sectionsCompleted / course.totalNumSections) * 100).toFixed(2)}%`"></b-progress-bar>
           </b-progress>
           </div>
          </div>
         </div>
      </div>
      <div class="container" data-aos="fade-up" style="padding-top: 60px">
        <div class="section-title">
          <h2>Completed Courses</h2>
        </div>
        <div class="row">
          <div
            v-for="course in completedCourses"
            :key="course.courseId"
            class="col-xl-3 col-md-6 d-flex align-items-stretch"
            data-aos="zoom-in"
            data-aos-delay="100"
          >
            <div class="icon-box">
              <div class="icon"><i class="bx bxl-dribbble"></i></div>
              <h4>
                <a href="">{{ course.courseName }}</a>
              </h4>
              <div class="course">
                <router-link
                  :to="{
                    path: '/LearnerViewSections',
                    query: {
                      classId: course.classId,
                      courseName: course.courseName,
                      sectionName: 'Section 1'
                    },
                  }"
                  class="btn btn-outline-dark"
                  >View Materials</router-link
                >
              </div>
            </div>
          </div>
        </div>
      </div>
      <div class="container" data-aos="fade-up" style="padding-top: 60px">
        <div class="section-title">
          <h2>Pending Courses</h2>
        </div>
        <table class="table">
          <thead>
            <tr>
              <th scope="col">Course ID</th>
              <th scope="col">Course Name</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="course in pendingCourses" :key="course.courseId">
              <td>{{ course.courseId }}</td>
              <td>{{ course.courseName }}</td>
            </tr>
          </tbody>
        </table>
      </div>
    </section>
  </div>
</template>

<script>
import axios from "axios";
export default {
  data: () => ({
    currentCourses: [],
    pendingCourses: [],
    completedCourses: [],
    learnerId: localStorage.getItem("userId"),
    max: 100,
    learner: {
      progress: 50,
    }
  }),
  async created() {
    const apiUrl1 = `http://localhost:5000/getEnrolmentsInProgress?learnerId=${this.learnerId}`;
    const apiUrl2 = `http://localhost:5000/getLearnerPendingEnrolments?learnerId=${this.learnerId}`;
    const apiUrl3 = `http://localhost:5000/getCompletedEnrolments?learnerId=${this.learnerId}`;
    const requestOne = await axios.get(apiUrl1);
    const requestTwo = await axios.get(apiUrl2);
    const requestThree = await axios.get(apiUrl3);

    await axios
      .all([requestOne, requestTwo, requestThree])
      .then(
        axios.spread((...responses) => {
          const responseOne = responses[0];
          const responseTwo = responses[1];
          const responseThree = responses[2];
          this.currentCourses = responseOne.data.data;
          this.pendingCourses = responseTwo.data.data;
          this.completedCourses = responseThree.data.data;

        })
      )
      .catch((errors) => {
        // react on errors.
        console.log(errors);
      });
  },
  methods: {
    isPastDate(enrolmentStartDate, enrolmentEndDate) {
      var today = new Date();
      var startDate = new Date(enrolmentStartDate);
      var endDate = new Date(enrolmentEndDate);
      if (today<startDate || today>endDate){
        return true;
      }
      return false;
    }
  }
};
</script>
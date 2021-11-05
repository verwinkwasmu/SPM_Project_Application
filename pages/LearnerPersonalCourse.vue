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
              <div class="course">
                <router-link
                  :to="{
                    path: '/LearnerViewSections',
                    query: {
                      classId: course.classId,
                    },
                  }"
                  class="course-btn"
                  >View Materials</router-link
                >
              </div>
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
                    },
                  }"
                  class="course-btn"
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
  }),
  async created() {
    const apiUrl1 = `http://localhost:5004/getEnrolmentsInProgress?learnerId=${this.learnerId}`;
    const apiUrl2 = `http://localhost:5004/getLearnerPendingEnrolments?learnerId=${this.learnerId}`;
    const apiUrl3 = `http://localhost:5004/getCompletedEnrolments?learnerId=${this.learnerId}`;
    const requestOne = axios.get(apiUrl1);
    const requestTwo = axios.get(apiUrl2);
    const requestThree = axios.get(apiUrl3);

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
          console.log(this.currentCourses);
          console.log(this.pendingCourses);
          console.log(this.completedCourses);
        })
      )
      .catch((errors) => {
        // react on errors.
        console.log(errors);
      });
  },
};
</script>
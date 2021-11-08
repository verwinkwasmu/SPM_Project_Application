<template>
  <div>
    <LearnerHeader/>
    <section id="hero" class="d-flex align-items-center">
      <div class="container">
        <div class="row">
          <div
            class="
              col-lg-6
              d-flex
              flex-column
              justify-content-center
              pt-4 pt-lg-0
              order-2 order-lg-1
            "
            data-aos="fade-up"
            data-aos-delay="200"
          >
            <h1>All-In-One Printing Solution</h1>
            <h4 id="home">
              We are a leading Printing Solution Equipment Servicing company. 
              We take pride in operating in the sale, lease, repair and maintenance of copying and printing solutions for businesses.               
            </h4>
=
          </div>
          <div
            class="col-lg-6 order-1 order-lg-2 hero-img"
            data-aos="zoom-in"
            data-aos-delay="200"
          >
            <img
              src="~/assets/img/hero-img.png"
              class="img-fluid animated"
              alt=""
            />
          </div>
        </div>
      </div>
    </section>
    
    <main id="main">

      <section id="services" class="services section-bg">
        <div class="container" data-aos="fade-up">
          <div class="section-title">
            <h2>My Current Courses</h2>
            <p>
            </p>
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
                class="btn btn-outline-dark"
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
      </section>
    </main>
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
    const apiUrl1 = `https://spm-flask.herokuapp.com/getEnrolmentsInProgress?learnerId=${this.learnerId}`;
    const apiUrl2 = `https://spm-flask.herokuapp.com/getLearnerPendingEnrolments?learnerId=${this.learnerId}`;
    const apiUrl3 = `https://spm-flask.herokuapp.com/getCompletedEnrolments?learnerId=${this.learnerId}`;
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
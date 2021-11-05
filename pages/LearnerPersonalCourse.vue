<template>
    <div id="app">
        <LearnerHeader/>
        <section id="services" class="services section-bg">
        <div class="container" data-aos="fade-up">
          <div class="section-title">
            <h2>Current Courses</h2>
          </div>
            <div class="row">
            <div
              class="col-xl-3 col-md-6 d-flex align-items-stretch"
              data-aos="zoom-in"
              data-aos-delay="100"
            >
              <div class="icon-box">
                <div class="icon"><i class="bx bxl-dribbble"></i></div>
                <h4><a href="">{{currentCourse.courseName}}</a></h4>
                <div class="course">
                  <a href="" class="course-btn">View Materials</a>
                </div>
              </div>
            </div>
          </div>
        </div>
        <div class="container" data-aos="fade-up" style="padding-top:60px;">
          <div class="section-title">
            <h2>Completed Courses</h2>
          </div>
          <div class="row">
            <div
              class="col-xl-3 col-md-6 d-flex align-items-stretch"
              data-aos="zoom-in"
              data-aos-delay="100"
            >
              <div class="icon-box">
                <div class="icon"><i class="bx bxl-dribbble"></i></div>
                <h4><a href="">{{completedCourse.courseName}}</a></h4>
                <div class="course">
                  <a href="" class="course-btn">View Materials</a>
                </div>
              </div>
            </div>
          </div>
        </div>
         <div class="container" data-aos="fade-up" style="padding-top:60px;">
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
                <tr>
                <td>{{PendingCourse.courseID}}</td>
                <td>{{PendingCourse.courseName}}</td>
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
  name: "App",
  data: () => ({

    currentCourse:
      {
        courseID: 'XRX-101',
        courseName: "Fundamentals of Xerox WorkCentre 7845",
      },
    PendingCourse: 
    {
        courseID: 'HP-112',
        courseName: "Boosting the HP 619 Performance",
    },
    completedCourse: 
    {
        courseID: 'XRX-103',
        courseName: "Final Xerox Work Centre 7900",
    },

  }),

  

};
</script>
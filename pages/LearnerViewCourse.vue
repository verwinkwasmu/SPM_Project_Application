<template>
    <div>
        <LearnerHeader/>
        <section id="services" class="services section-bg">
        <div class="container" data-aos="fade-up">
          <div class="section-title">
            <h2>Available Courses</h2>
          </div>

          <div class="row">
            <div
              v-for="course in courses"
              :key="course.courseId"
              class="col-xl-3 col-md-6 d-flex align-items-stretch"
              data-aos="zoom-in"
              style="padding-bottom:50px;"
              data-aos-delay="100"
            >
              <div class="icon-box">
                <!-- <div class="icon"><i class="bx bxl-dribbble"></i></div>
                <h4><a href="">Fundamentals of Xerox WorkCentre 7845</a></h4>
                <div class="course">
                  <a href="LearnerViewCourseDetails" class="course-btn">View Details</a> -->
                <!-- </div> -->
                <h4><a href="">{{ course.courseName }}</a></h4>
                <div class="viewClass">
                  <a class="viewClass-btn" @click="setCourseIdSession(course.courseId)">View Course Details</a>
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
    courses: [],
    error: false,
    message: "",
  }),
  async mounted() {
    const apiUrl = "http://localhost:5002/viewLearnerCourses";
    try {
      let response = await axios.get(apiUrl);
      this.courses = response.data.data;
      this.error = false;
    } catch (err) {
      console.log(err);
      this.error = true;
      this.message = err;
    }
  },
  methods: {
    setCourseIdSession(courseId){
      localStorage.removeItem('courseId')
      localStorage.setItem('courseId', courseId)
      this.$router.push('/LearnerViewCourseDetails')
    }
  }
  
  
};
</script>
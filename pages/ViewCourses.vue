<template>
  <div>
    <Header />
    <section id="services" class="services section-bg">
      <div class="container" data-aos="fade-up">
        <div class="section-title">
          <h2>Courses</h2>
          <p></p>
          <div class="createClass">
            <a href="/CreateCourse" class="btn btn-success">Create Course</a>
          </div>
        </div>

        <div class="row">
          <div v-if="error" class="alert alert-danger" role="alert">
            {{ message }}
          </div>

          <div
            v-for="course in courses"
            :key="course.courseId"
            class="col-xl-3 col-md-6 d-flex align-items-stretch mt-4 mt-xl-0"
            data-aos="zoom-in"
            data-aos-delay="400"
            style="padding-bottom: 30px;"
          >
            <div class="icon-box">
              <div class="icon"><i class="bx bx-layer"></i></div>
              <h4>
                <a href="">{{ course.courseName }}</a>
              </h4>
              <div class="viewclass">
                <button class="btn btn-outline-dark" @click="setCourseIdSession(course.courseId)">View Classes</button>
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
    const apiUrl = "https://spm-flask.herokuapp.com/getCourses";
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
      this.$router.push('/ViewClasses')
    }
  }
  
  
};
</script>

<template>
    <div>
        <TrainerHeader/>
        <section id="services" class="services section-bg">
        <div class="container" data-aos="fade-up">
          <div class="section-title">
            <h2>My Teaching Courses</h2>
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
            >
            
              <div class="icon-box">
                <div class="icon"><i class="bx bxl-dribbble"></i></div>
                <h4><a href="">{{ course.courseName }}</a></h4>
                <div class="viewClass">
                  <a class="btn btn-outline-dark" @click="setCourseIdSession(course.courseId)">View Classes</a>
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
    trainerId: localStorage.getItem('userId'),
    courses: [],
    error: false,
    message: "",
  }),
  async mounted() {
    const apiUrl = `https://spm-flask.herokuapp.com/getTrainerCourses/${this.trainerId}`;
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
      this.$router.push('/TrainerViewClasses')
    }
  }

  
  
};
</script>
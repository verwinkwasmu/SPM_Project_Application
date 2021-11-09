<!-- Please remove this file from your project -->
<template>
  <div>
    <Header />
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
            <h2>Courses</h2>
            <p>
            </p>
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
     
    
    </main>
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
      console.log(this.courses)
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

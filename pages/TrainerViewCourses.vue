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
                  <a class="viewClass-btn" @click="setCourseIdSession(course.courseId)">View Classes</a>
                </div>
              </div>
            </div>

            <!-- <div
              class="col-xl-3 col-md-6 d-flex align-items-stretch mt-4 mt-xl-0"
              data-aos="zoom-in"
              data-aos-delay="100"
            > -->
              <!-- <div class="icon-box">
                <div class="icon"><i class="bx bxl-dribbble"></i></div>
                <h4><a href="">Fundamentals of Xerox WorkCentre 7845</a></h4>
                <div class="course">
                  <a href="TrainerViewClasses" class="course-btn">View Classes</a>
                </div>
              </div>
            </div> -->
            
            <!-- <div
              class="col-xl-3 col-md-6 d-flex align-items-stretch mt-4 mt-md-0"
              data-aos="zoom-in"
              data-aos-delay="200"
            >
              <div class="icon-box">
                <div class="icon"><i class="bx bx-file"></i></div>
                <h4><a href="">Programming for Xerox WorkCentre with Card Access and Integration</a></h4>
                <div class="course">  
                  <a href="#" class="course-btn">View Classes</a>
                </div>             
               </div>
            </div>

            <div
              class="col-xl-3 col-md-6 d-flex align-items-stretch mt-4 mt-xl-0"
              data-aos="zoom-in"
              data-aos-delay="300"
            >
              <div class="icon-box">
                <div class="icon"><i class="bx bx-tachometer"></i></div>
                <h4><a href="">Advanced Xerox WorkCentre 7900</a></h4>
                <div class="course">
                  <a href="#" class="course-btn">View Classes</a>
                </div>
              </div>
            </div>

            <div
              class="col-xl-3 col-md-6 d-flex align-items-stretch mt-4 mt-xl-0"
              data-aos="zoom-in"
              data-aos-delay="400"
            >
              <div class="icon-box">
                <div class="icon"><i class="bx bx-layer"></i></div>
                <h4><a href="">Final Xerox WorkCentre 7900</a></h4>
                <div class="course">
                  <a href="#" class="course-btn">View Classes</a>
                </div>
              </div>
              
            </div> -->
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
    const apiUrl = `http://localhost:5002/getTrainerCourses/${this.trainerId}`;
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
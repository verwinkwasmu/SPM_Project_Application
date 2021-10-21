<template>
  <div>
    <Header />
    <section id="team" class="team section-bg">
      <div class="container" data-aos="fade-up">
        <div class="section-title">
          <!--<div class="createClass">
                  <a href="createClass" class="createClass-btn">Create Class</a>
              </div>-->
          <h2>{{ this.$route.query.courseName }}</h2>
          <div class="createClass">
            <router-link  :to="{path: '/CreateClass', query: {courseId: this.$route.query.courseId, courseName: this.$route.query.courseName}}" class="createClass-btn">Create Class</router-link>
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
                <p>
                  Explicabo voluptatem mollitia et repellat qui dolorum quasi
                </p>
              </div>
              <div class="viewClass">
                <router-link :to="{path: '/EditClass', query: {classId: _class.classId, courseId: _class.courseId}}" class="viewClass-btn">Edit Class</router-link>
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
    classes: [],
    error: false,
    message: ""
  }),
  async mounted() {
    const apiUrl = `http://localhost:5002/getClasses/${this.$route.query.courseId}`;
    try {
      let response = await axios.get(apiUrl);
      console.log(response)
      this.classes = response.data.data;
      console.log(this.classes);
      this.error = false;
    } catch (err) {
      console.log(err);
      this.error = true;
      this.message = err;
    }
  },
};
</script>

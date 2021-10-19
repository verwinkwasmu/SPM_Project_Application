<template>
  <div>
    <Header />

    <!--<Homepage/>
       -->
    <section id="contact" class="contact">
      <div class="container" data-aos="fade-up">
        <div class="section-title">
          <h2>Create Course</h2>
        </div>

        <div class="row">
          <div class="col-lg-8" id="createCourse">
            <form
              action="forms/contact.php"
              method="post"
              role="form"
              class="php-email-form"
            >
              <div class="row">
                <div class="form-group">
                  <label for="name">Course ID</label>
                  <input
                    v-model="courseId"
                    type="text"
                    class="form-control"
                    name="subject"
                    id="subject"
                    required
                  />
                </div>
              </div>
              <div class="row">
                <div class="form-group">
                  <label for="name">Course Name</label>
                  <input
                    v-model="courseName"
                    type="text"
                    class="form-control"
                    name="subject"
                    id="subject"
                    required
                  />
                </div>
              </div>

              <div class="form-group">
                <label for="name">Course Description</label>
                <input
                  v-model="courseDescription"
                  class="form-control"
                  name="message"
                  rows="10"
                  required
                />
              </div>

              <div class="form-group">
                <label for="name">Prerequisite</label>
                <textarea
                  v-model="prerequisites"
                  class="form-control"
                  name="message"
                  rows="10"
                  required
                ></textarea>
              </div>
            </form>
          </div>
        </div>
      </div>
    </section>

    <div class="buttongroup">
      <div class="classCreate">
        <a href="#" class="classCreate-btn" @click="createCourse"
          >Create Course</a
        >
      </div>
      <div class="cancel">
        <a href="ViewCourse" class="cancel-btn">Cancel</a>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
export default {
  data: () => ({
    courseName: "",
    courseDescription: "",
    prerequisites: "",
    courseId: "",
    failed: false,
    errorMessage: "",
  }),
  methods: {
    createCourse(event) {
      event.preventDefault();

      const course_details = {
        courseId: this.courseId,
        courseName: this.courseName,
        courseDescription: this.courseDescription,
        prerequisites: this.prerequisites,
      };
      console.log(course_details)
      axios
        .post("http://localhost:5002/createCourse", course_details)
        .then((response) => {
          this.data = response;
          console.log(this.data)
          if (this.data.status != 201) {
            this.failed = true
            this.errorMessage = "unable to create course"
            console.log(this.errorMessage)
          }
          else {
            alert("its g")
          }
        }).catch((error) =>  {
          this.errorMessage = error.message;
        });
    },
  },
};
</script>

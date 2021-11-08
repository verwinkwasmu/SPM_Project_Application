<template>
  <div>
    <Header />

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
            <br />
            <div
              v-if="error == true"
              class="alert alert-danger alert-dismissible fade show"
              role="alert"
            >
              {{ message }}
              <button
                type="button"
                class="btn-close"
                data-bs-dismiss="alert"
                aria-label="Close"
              ></button>
            </div>
            <div
              v-else-if="error == false"
              class="alert alert-success alert-dismissible fade show"
              role="alert"
            >
              {{ message }}
              <button
                type="button"
                class="btn-close"
                data-bs-dismiss="alert"
                aria-label="Close"
              ></button>
            </div>
          </div>
        </div>
      </div>
    </section>

    <div class="buttongroup" style="margin-left: 45%;">
      <div class="classCreate">
        <a href="#" class="btn btn-success" @click="createCourse"
          >Create Course</a
        >
      </div>
      <div class="cancel">
        <a href="/ViewCourses" class="btn btn-danger">Cancel</a>
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
    error: null,
    message: "",
    data: null,
  }),
  methods: {
    async createCourse(event) {
      event.preventDefault();
	  if (!this.courseName || !this.courseDescription || !this.courseId){
		  this.error = true;
		  this.message = "Please make sure Course Name, Course Description and Course ID are not empty!"
		  return
	  }
      const apiUrl = "http://localhost:5000/createCourse";
      const course_details = {
        courseId: this.courseId,
        courseName: this.courseName,
        courseDescription: this.courseDescription,
        prerequisites: this.prerequisites,
      };
	  try{
		  let response = await axios.post(apiUrl, course_details)
		  console.log(response)
		  if (response.status == 201) {
            this.data = response.data;
            this.error = false;
            this.message = "Course Successfully Created! 😃";
          } else {
            this.error = true;
            this.message = "Course already exists!";
          }
	  }catch(err){
		  console.log(err)
		  this.error = true;
		  this.message = err
	  }
      
    },
  },
};
</script>

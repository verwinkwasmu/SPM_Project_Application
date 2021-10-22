<template>
  <div>
    <Header />

    <!--<Homepage/>
       -->
    <section id="contact" class="contact">
      <div class="container" data-aos="fade-up">
        <div class="section-title">
          <h2>Create Class</h2>
        </div>

        <div class="row">
          <div class="col-lg-6 mt-5 mt-lg-0 d-flex align-items-stretch">
            <form
              action="forms/contact.php"
              method="post"
              role="form"
              class="php-email-form"
            >
              <div class="row">
                <div class="form-group">
                  <label for="name">Class Title</label>
                  <input
                    v-model="classTitle"
                    type="text"
                    class="form-control"
                    name="subject"
                    id="subject"
                    required
                  />
                </div>

                <div class="form-group">
                  <label for="name">Class Size</label>
                  <input
                    v-model="classSize"
                    type="number"
                    name="name"
                    class="form-control"
                    id="name"
                    required
                  />
                </div>
                <div class="form-group">
                  <label for="name">Start Time</label>
                  <b-form-timepicker
                    v-model="startTime"
                    locale="en"
                  ></b-form-timepicker>
                </div>
                <div class="form-group">
                  <label for="name">End Time</label>
                  <b-form-timepicker
                    v-model="endTime"
                    locale="en"
                  ></b-form-timepicker>
                </div>

                <br />
                <br />
                <br />
                <br />
                <br />

                <!-- <div class="form-group">
                    <label for="name">Trainer Assigned</label>
                    <input
                      type="dropdown"
                      class="form-control"
                      name="email"
                      id="email"
                      required
                    />

                  <br>

                    <label for="cars">Assign a Trainer:</label>
                      <select name="cars" id="cars">
                        <optgroup label="Sales Department">
                          <option value="Halim">Halim</option>
                          <option value="Mark">Mark</option>
                        </optgroup>
                        <optgroup label="Leasing Department">
                          <option value="Bob">Bob</option>
                          <option value="Ali">Ali</option>
                        </optgroup>
                      </select>
                    
                  
                    
                  </div> -->
              </div>

              <!-- <div class="form-group">
                  <label for="name">Message</label>
                  <textarea
                    class="form-control"
                    name="message"
                    rows="10"
                    required
                  ></textarea>
                </div>
                <div class="my-3">
                  <div class="loading">Loading</div>
                  <div class="error-message"></div>
                  <div class="sent-message">
                    Your message has been sent. Thank you!
                  </div>
                </div>
                <div class="text-center">
                  <button type="submit">Send Message</button>
                </div> -->
            </form>
          </div>
          <div class="col-lg-6 d-flex align-items-stretch">
            <div class="info">
              <div>
                <h5>Class Start Date:</h5>
                <client-only>
                  <date-picker
                    placeholder="MM/DD/YYYY"
                    format="MM/dd/yyyy"
                    v-model="startDate"
                  />
                </client-only>
                <div class="date">
                  <h5>Class End Date:</h5>

                  <client-only>
                    <date-picker
                      placeholder="MM/DD/YYYY"
                      format="MM/dd/yyyy"
                      v-model="endDate"
                    />
                  </client-only>
                </div>
              </div>
            </div>
            <div class="info">
              <h5>Enrolment Start Date:</h5>
              <client-only>
                <date-picker
                  placeholder="MM/DD/YYYY"
                  format="MM/dd/yyyy"
                  v-model="enrolmentStart"
                />
              </client-only>
              <div class="date">
                <h5>Enrolment End Date:</h5>
                <client-only>
                  <date-picker
                    placeholder="MM/DD/YYYY"
                    format="MM/dd/yyyy"
                    v-model="enrolmentEnd"
                  />
                </client-only>
              </div>
            </div>
          </div>
        </div>
        <br>
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
    </section>

    <div class="buttongroup">
      <div class="classCreate">
        <a href="#" class="classCreate-btn" @click="createClass"
          >Create Class</a
        >
      </div>
      <div class="cancel">
        <router-link class="cancel-btn" :to="{path: '/ViewClasses', query: {courseId: this.$route.query.courseId, courseName: this.$route.query.courseName}}">Cancel</router-link>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  data: () => ({
    classTitle: "",
    classSize: "",
    startTime: "",
    endTime: "",
    startDate: "",
    endDate: "",
    enrolmentStart: "",
    enrolmentEnd: "",
    message: "",
    error: null,
  }),
  methods: {
    async createClass(event) {
      event.preventDefault();
      
      // if (!this.courseName || !this.courseDescription || !this.courseId) {
      //   this.error = true;
      //   this.message =
      //     "Please make sure Course Name, Course Description and Course ID are not empty!";
      //   return;
      // }
      const apiUrl = "http://localhost:5002/createClass";

      const class_details = {
        classId: this.$route.query.courseId + " " + this.classTitle,
        courseId: this.$route.query.courseId,
        classSize: this.classSize,
        classTitle: this.classTitle,
        classTiming: this.startTime + ' to ' + this.endTime,
        classTimeline: (this.startDate).toISOString().substring(0, 10) + ' to ' + (this.endDate).toISOString().substring(0, 10),
        enrolmentPeriod: (this.enrolmentStart).toISOString().substring(0, 10) + " to " + (this.enrolmentEnd).toISOString().substring(0, 10),
        trainerAssigned: null,
        trainerName: null
      };
      
      try {
        let response = await axios.post(apiUrl, class_details);
        console.log(response);
        if (response.status == 201) {
          this.data = response.data;
          this.error = false;
          this.message = "Class Successfully Created! 😃";
        } else {
          this.error = true;
          this.message = "Class already exists!";
        }
      } catch (err) {
        console.log(err);
        this.error = true;
        this.message = err;
      }
    },
  },
};
</script>

<template>
  <div>
    <LearnerHeader/>
    <Modal :message="message"/>
    <section id="team" class="team section-bg">
      <!--box-->
      <div class="container" data-aos="fade-up">
        <div class="section-title">
          <h2>{{ course.courseName }}<br /></h2>
        </div>
        <div class="LearnerEnrolStatus" v-if="enrolmentStatus == 'PENDING'">
          <span class="badge badge-secondary">Pending Approval</span>
        </div>
        <div class="LearnerEnrolStatus" v-if="enrolmentStatus == 'ACCEPTED'">
          <span class="badge badge-success">Approved! 👍</span>
        </div>
        <div class="row">
          <div class="col-lg-8" id="createCourse" style="padding-bottom: 100px">
            <div
              class="member d-flex align-items-start"
              data-aos="zoom-in"
              data-aos-delay="100"
            >
              
              <div class="member-info">
                <!-- <h4>{{ course.courseName }}</h4> -->
                <h4>Course ID:</h4>
                <p>{{ course.courseId }}</p>
                <br />
                <h4>Course Description:</h4>
                <p>{{ course.courseDescription }}</p>
                <br />
                <h4>Prerequisite Courses:</h4>
                <ul v-if="course.prerequisites != ''">
                  <li>{{ course.prerequisites }}</li>
                </ul>
                <ul v-else>
                  <li>No prerequisites required</li>
                </ul>
              </div>
              <div
                class="LearnerEnrol"
                v-if="enrolmentStatus == 'NOT ENROLLED'"
              >
                <router-link
                  :to="{ path: '/LearnerViewClass' }"
                  class="btn btn-outline-success"
                  >Enrol into Course</router-link
                >
              </div>
              <div
                class="LearnerWithdraw"
                v-if="
                  enrolmentStatus == 'PENDING' || enrolmentStatus == 'ACCEPTED'
                "
              >
                <button
                  class="btn btn-outline-danger"
                  @click="withdraw(course.courseId)"
                >
                  Withdraw from Course
                </button>
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
    course: {},
    error: false,
    message: "",
    enrolment: {},
    courseId: localStorage.getItem("courseId"),
    learnerId: localStorage.getItem("userId"),
    enrolmentStatus: "",
  }),
  async mounted() {
    const apiUrl1 = `https://spm-flask.herokuapp.com/getCourse/${this.courseId}`;
    const apiUrl2 = `https://spm-flask.herokuapp.com/viewUserEnrolmentStatus?learnerId=${this.learnerId}&courseId=${this.courseId}`;

    try {
      let response1 = await axios.get(apiUrl1);
      let response2 = await axios.get(apiUrl2);
      this.course = response1.data;

      this.enrolmentStatus = response2.data.enrolmentStatus;
      this.error = false;
    } catch (err) {
      console.log(err);
      this.error = true;
      this.message = err;
    }
  },
  methods: {
    async withdraw(courseId) {
      const apiUrl = "https://spm-flask.herokuapp.com/withdrawLearner";
      const data = {
        courseId: courseId,
        learnerId: localStorage.getItem("userId"),
      };

      try {
        let response = await axios.delete(apiUrl, { data: data });
        if (response.status == 200) {
          this.message = response.data.message;
          this.$bvModal.show("bv-modal-example");
          setTimeout(
            function () {
              window.location.reload();
            }.bind(this),
            2000
          );
        } else {
          alert("Please Try again!");
        }
      } catch (err) {
          console.log(err)
      }
    },
  },
};
</script>


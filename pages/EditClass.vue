<template>
  <div>
    <Header />
    <Modal :message="message" />

    <section id="team" class="team section-bg">
      <!--box-->
      <div class="container block" data-aos="fade-up">
        <div class="row pb-5 mb-2">
          <div class="viewClass">
            <router-link :to="{ path: '/ViewClasses' }" class="btn btn-primary"
              >Back to see all Classes</router-link
            >
          </div>
        </div>
        <div class="section-title">
          <h2>{{ myClass.classId }}</h2>
          <h3>{{ course.courseName }}</h3>
        </div>
        <div class="row">
          <div class="col-lg-8" id="createCourse" style="padding-bottom: 50px">
            <div
              class="member d-flex align-items-start"
              data-aos="zoom-in"
              data-aos-delay="100"
            >
              <div class="member-info">
                <h4>Course ID:</h4>
                <p>{{ course.courseId }}</p>
                <br />
                <h4>Course Description:</h4>
                <p>{{ course.courseDescription }}</p>
                <br />
                <h4>Prerequisite Courses:</h4>
                <ul v-if="course.prerequisites == ''">
                  <li>No Prerequisites</li>
                </ul>
                <ul v-else>
                  <li>{{ course.prerequisites }}</li>
                </ul>
                <h4>Maximum Class Size:</h4>
                <p>{{ myClass.classSize }}</p>
                <br />
                <h4>Current Class Size:</h4>
                <p>{{ learners.length }}</p>
                <br />
                <h4>Period of Enrollment:</h4>
                <p>
                  {{ myClass.enrolmentStartDate }} to
                  {{ myClass.enrolmentEndDate }}
                </p>
                <br />
                <h4>Period of Class:</h4>
                <p>
                  {{ myClass.startDate }}, {{ myClass.startTime }} <b>to</b>
                  {{ myClass.endDate }}, {{ myClass.endTime }}
                </p>
                <br />
              </div>
            </div>
          </div>

          <div class="col-lg-8 mt-4 mt-lg-0" id="createCourse">
            <div class="member-info" style="padding-bottom: 100px">
              <h5>Assign a Trainer:</h5>
              <b-select v-model="selectedTrainer">
                <option
                  v-for="trainer in trainers"
                  :value="trainer"
                  :key="trainer.userId"
                >
                  {{ trainer.employeeName }}
                </option>
              </b-select>
              <br />
              <div
                v-if="error == true"
                class="alert alert-danger alert-dismissible fade show mt-5"
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
              <div class="addEngineer mt-5">
                <a href="" class="btn btn-success" @click="assignTrainer"
                  >Assign Trainer</a
                >
              </div>
            </div>

            <section id="team" class="team section-bg">
              <div>
                <h4>Current Learners enrolled into this class:</h4>

                <table class="table table-striped">
                  <thead>
                    <tr>
                      <th scope="col">Learner Id</th>
                      <th scope="col">Learner Name</th>
                      <th scope="col">Remove?</th>
                    </tr>
                  </thead>
                  <tbody>
                    <tr v-for="learner in learners" :key="learner.learnerId">
                      <td>{{ learner.learnerId }}</td>
                      <td>{{ learner.learnerName }}</td>
                      <td>
                        <a
                          class="remove-btn"
                          @click="removeLearner(learner.learnerId)"
                          >Remove</a
                        >
                      </td>
                    </tr>
                  </tbody>
                </table>
              </div>
            </section>
            <div class="buttongroup">
              <div class="classCreate">
                <router-link
                class="btn btn-success"
                  :to="{
                    path: '/AddEngineer',
                    query: {
                      classId: this.$route.query.classId,
                    },
                  }"
                  >Add Learners</router-link
                >
              </div>
              <div class="cancel">
                <router-link
                class="btn btn-danger"
                  :to="{
                    path: '/ViewClasses',
                  }"
                  >Cancel</router-link
                >
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
    courseId: localStorage.getItem("courseId"),
    course: {},
    myClass: {},
    trainers: [],
    learners: [],
    error: null,
    message: "",
    selectedTrainer: "",
  }),
  mounted() {
    const apiUrl1 = `http://localhost:5000/getCourse/${this.courseId}`;
    const apiUrl2 = `http://localhost:5000/getClass/${this.$route.query.classId}`;
    const apiUrl3 = `http://localhost:5000/getTrainers`;
    const apiUrl4 = `http://localhost:5000/enrolment/${this.$route.query.classId}`;
    const requestOne = axios.get(apiUrl1);
    const requestTwo = axios.get(apiUrl2);
    const requestThree = axios.get(apiUrl3);
    const requestFour = axios.get(apiUrl4);

    axios
      .all([requestOne, requestTwo, requestThree, requestFour])
      .then(
        axios.spread((...responses) => {
          const responseOne = responses[0];
          const responseTwo = responses[1];
          const responseThree = responses[2];
          const responseFour = responses[3];

          this.course = responseOne.data;
          this.myClass = responseTwo.data;
          this.trainers = responseThree.data.data;
          this.learners = responseFour.data.data;
        })
      )
      .catch((errors) => {
        // react on errors.
        console.log(errors);
      });
  },
  methods: {
    async assignTrainer(event) {
      event.preventDefault();

      const apiUrl = "http://localhost:5000/assignTrainerClass";

      const trainerData = {
        classId: this.myClass.classId,
        trainerAssigned: this.selectedTrainer.userId,
        trainerName: this.selectedTrainer.employeeName,
      };
      try {
        let response = await axios.put(apiUrl, trainerData);
        if (response.status == 200) {
          this.data = response.data;
          this.error = false;
          this.message = "Trainer Successfully Assigned! 😃";
        } else {
          this.error = true;
          this.message = "Error! Please try again";
        }
      } catch (err) {
        console.log(err);
        this.error = true;
        this.message = err;
      }
    },
    async removeLearner(learnerId) {
      const apiUrl = `http://localhost:5000/removeLearner`;
      const learnerData = {
        classId: this.$route.query.classId,
        learnerId: learnerId,
      };
      try {
        let response = await axios.delete(apiUrl, { data: learnerData });
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
        console.log(err);
        alert(err);
      }
    },
  },
};
</script>  

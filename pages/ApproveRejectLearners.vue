<template>
  <div>
    <Header />
    <Modal :message="message" />
    <section id="team" class="team section-bg">
      <div class="container" data-aos="fade-up">

        <div class="row pb-5 mb-2 ml-0">
          <div class="viewClass">
            <router-link :to="{path: '/EditClass', query: {classId: this.$route.query.classId}}" class="btn btn-primary" >Back to edit Classes</router-link>
          </div>
        </div>
        
        <div class="row">
          <div class="col-lg-8" id="createCourse" style="padding-bottom: 50px">
            <div class="addEngineer">
              <h5>Pending list:</h5>
            </div>
            <div class="container" id="app">
              <div class="row">
                <div class="col-12">
                  <table class="table table-bordered">
                    <thead>
                      <tr>
                        <th scope="col">Learner ID</th>
                        <th scope="col">Learner Name</th>
                      </tr>
                    </thead>
                    <tbody>
                      <tr v-for="learner in learners" :key="learner.learnerId">
                        <td>{{ learner.learnerId }}</td>
                        <td>{{ learner.learnerName }}</td>
                        <td>
                          <div class="custom-control custom-checkbox">
                            <input
                              type="checkbox"
                              class="custom-control-input"
                              :id="learner.learnerId"
                              :value="learner.learnerId"
                              v-model="learnerIds"
                            />
                            <label
                              class="custom-control-label"
                              :for="learner.learnerId"
                            ></label>
                          </div>
                        </td>
                      </tr>
                    </tbody>
                  </table>
                </div>
                <div class="buttongroup">
                  <div class="classCreate">
                    <button
                      @click="updateEnrolment('ACCEPTED')"
                      class="btn btn-success"
                    >
                      Approve
                    </button>
                    <button
                      @click="updateEnrolment('REJECTED')"
                      class="btn btn-danger"
                    >
                      Reject
                    </button>
                  </div>
                 
                  <!-- Link to DB to refresh page with updated list-->
                </div>
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
  name: "app",
  data: () => ({
    learners: [],
    learnerIds: [],
    message: "",
  }),

  async created() {
    const apiUrl = `https://spm-flask.herokuapp.com/viewPendingEnrolments?classId=${this.$route.query.classId}`;
    try {
      let response = await axios.get(apiUrl);
      this.learners = response.data.data;
    } catch (err) {
      console.log(err);
    }
  },
  methods: {
    async updateEnrolment(status) {
      const apiUrl = "https://spm-flask.herokuapp.com/updateEnrolmentRequests";

      const pending_data = {
        classId: this.$route.query.classId,
        learnerIds: this.learnerIds,
        status: status,
      };
      try {
        let response = await axios.put(apiUrl, pending_data);
        if (response.status == 200) {
          this.message = "Enrolment Successfully Updated!";
          this.$bvModal.show("bv-modal-example");
          setTimeout(function () {
            window.location.reload()
          }.bind(this), 2000);
        } else {
          alert("Please Try again!");
        }
      } catch (err) {
        console.log(err);
      }
    },
  },
};
</script>


<template>
  <div>
    <Header />
    <section id="team" class="team section-bg">
      <div class="container" data-aos="fade-up">
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
                <div class="ApproveRejectPage">
                  <div class="approve">
                    <button @click="updateEnrolment('ACCEPTED')" class="approve-btn">Approve</button>
                  </div>
                  <div class="reject">
                    <button @click="updateEnrolment('REJECTED')" class="reject-btn">Reject</button>
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

  }),

  async created() {
    const apiUrl = `http://localhost:5004/viewPendingEnrolments?classId=${this.$route.query.classId}`;
    try {
      let response = await axios.get(apiUrl);
      this.learners = response.data.data;
      console.log(this.learnerIds)
    } catch (err) {
      console.log(err);
    }
  },
  methods: {
    async updateEnrolment(status) {
      console.log(this.learnerIds);
      const apiUrl = "http://localhost:5004/updateEnrolmentRequests";

      const pending_data = {
        classId: this.$route.query.classId,
        learnerIds: this.learnerIds,
        status: status
      };
      try {
        let response = await axios.put(apiUrl, pending_data);
        console.log(response)
        if (response.status == 200) {
          alert("Enrolment Successfully Updated!");
          window.location.reload();
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


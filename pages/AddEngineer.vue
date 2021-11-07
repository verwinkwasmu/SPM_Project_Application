<template>
  <div>
    <Header />
    <section id="team" class="team section-bg">
      <div class="container" data-aos="fade-up">
        <div class="row">
          <div class="col-lg-8" id="createCourse" style="padding-bottom: 50px">
            <div class="addEngineer">
              <h5>Total List of Qualified Engineers:</h5>
            </div>

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
            <div
              v-if="error == true"
              class="alert alert-danger text-center"
              role="alert"
            >
              {{ message }}

            </div>
            <div
              v-else-if="error == false"
              class="alert alert-success text-center"
              role="alert"
            >
              {{ message }}

            </div>
            <div class="Add">
              <a href="" class="Add-btn" @click="enrolLearners">Add</a>
            </div>
            <!-- Link to DB to refresh page with updated list-->
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
    learners: [],
    learnerIds: [],
    error: null,
    message: "",
  }),
  async mounted() {
    const apiUrl = `http://localhost:5004/enrolment/qualifiedlearners/${this.$route.query.classId}`;
    try {
      let response = await axios.get(apiUrl);
      this.learners = response.data.data;
    } catch (err) {
      console.log(err);
      this.error = true;
      this.message = err;
    }
  },
  methods: {
    async enrolLearners(event) {
      event.preventDefault();
      this.error = null;

      const apiUrl = `http://localhost:5004/enrolment/enrolLearners`;

      const learners_data = {
        classId: this.$route.query.classId,
        learnerIds: this.learnerIds,
      };

      try {
        let response = await axios.post(apiUrl, learners_data);
        if (response.status == 201) {
          this.error = false;
          this.message = "Learners Enrolled! 😃";

          setTimeout(function(){
            window.location.reload()
          }.bind(this), 2000);

        } else {
          this.error = true;
          this.message = "Please Try Again!"
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

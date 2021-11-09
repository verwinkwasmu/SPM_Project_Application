<template>
  <div id="app">
    <TrainerHeader />
    <section id="team" class="team section-bg">
      <div class="container" data-aos="fade-up">
        <button
          onclick="document.location='TrainerViewClasses'"
          type="button"
          class="btn btn-primary"
        >
          Back to All classes
        </button>
        <div class="section-title">
          <h2>View Class Learner's progress</h2>
          <h3>{{courseName}}</h3>
          <h5>{{className}}</h5>
        </div>
        <div class="row">
          <table class="table">
            <thead>
              <tr>
                <th scope="col">Learner ID</th>
                <th scope="col">Learner Name</th>
                <th scope="col">Progress</th>
              </tr>
            </thead>
            <tbody>
              <tr v-for="learner in learners" :key="learner.learnerId">
                <th scope="row">{{ learner.learnerId }}</th>
                <td>{{ learner.learnerName }}</td>
                <td>
                  <b-progress
                    :max="learner.totalNumSections"
                    show-progress
                    animated
                    ><b-progress-bar
                      :value="learner.sectionsCompleted"
                      :label="`${(
                        (learner.sectionsCompleted / learner.totalNumSections) *
                        100
                      ).toFixed(2)}%`"
                    ></b-progress-bar
                  ></b-progress>
                </td>
              </tr>
              
            </tbody>
          </table>
        </div>
      </div>
    </section>
  </div>
</template>

<script>
import axios from "axios";

export default {

  data: () => ({
    classId: '',
    learners: [],
    className: '',
    courseName: '',
  }),
  async created() {
    this.classId = this.$route.query.classId;
    this.className = this.$route.query.classId.split(" ")[1] + ' ' + this.$route.query.classId.split(" ")[2];
    this.courseName = this.$route.query.courseName;

    const apiUrl = `https://spm-flask.herokuapp.com/enrolment/${this.classId}`;
    
    try {
      let response = await axios.get(apiUrl);
      this.learners = response.data.data;
      
    } catch (err) {
      console.log(err);
    }
  },
};
</script>

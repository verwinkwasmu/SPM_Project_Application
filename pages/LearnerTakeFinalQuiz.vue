<template>
  <div id="axiosForm">
    <LearnerHeader />
    <section id="team" class="team section-bg">
      <div class="" data-aos="fade-up">
        <div id="App" class="container">
          <div class="section-title">
            <h2>{{ courseName }}</h2>
            <h3>{{sectionId}}</h3>
          </div>
          <div class="timer">
            Time Remaining: <strong>{{ displayTime }} </strong>
          </div>

          <div class="" v-for="(question, index) in questions" :key="index">
            <h4>{{ index + 1 }}. {{ question.question }}</h4>
            <br />

            <div class="optionContainer">
              <div class="option">
                <label id="quizrbtn"
                  ><input
                    type="radio"
                    :value="question.option[0]"
                    :name="question.questionId"
                    v-model="question.value"
                  />
                  {{ question.option[0] }}</label
                >
              </div>

              <div class="option">
                <label id="quizrbtn"
                  ><input
                    type="radio"
                    :value="question.option[1]"
                    :name="question.questionId"
                    v-model="question.value"
                  />
                  {{ question.option[1] }}</label
                >
              </div>

              <div class="option" v-if="question.option[2]">
                <label id="quizrbtn"
                  ><input
                    type="radio"
                    :value="question.option[2]"
                    :name="question.questionId"
                    v-model="question.value"
                  />
                  {{ question.option[2] }}</label
                >
              </div>

              <div class="option" v-if="question.option[3]">
                <label id="quizrbtn"
                  ><input
                    type="radio"
                    :value="question.option[3]"
                    :name="question.questionId"
                    v-model="question.value"
                  />
                  {{ question.option[3] }}</label
                >
              </div>
            </div>

            <hr />
          </div>

          <div class="form-group" id="submitquiz">
            <b-button variant="primary" @click="$bvModal.show('modal-scoped')"
              >Submit Quiz</b-button
            >
            <b-modal id="modal-scoped">
              <template #modal-header="{}">
                <h5>Submit Quiz</h5>
              </template>
              <template #default="{}">
                <p>Do you want to submit your quiz?</p>
              </template>
              <template #modal-footer="{ hide}">
                <b-button size="sm" variant="danger" @click="hide('forget')">
                  No
                </b-button>
                <b-button
                  size="sm"
                  variant="success"
                  @click="submitQuiz"
                >
                  Yes
                </b-button>
              </template>
            </b-modal>
          </div>
        </div>
      </div>
    </section>
  </div>
</template>

<script>
import axios from "axios";
export default {
  name: "App",
  data: () => ({
    courseName: "",
    time: "-",
    displayTime: "",
    msgBox: "",
    classId: "",
    sectionId: "",
    questions: [],
  }),
  async mounted() {
    this.sectionId = this.$route.query.sectionId;
    this.classId = this.$route.query.classId;
    this.courseName = this.$route.query.courseName;
    this.timer = setInterval(this.countdown, 1000);

    const apiUrl = `https://spm-flask.herokuapp.com/quiz/${this.classId}/${this.sectionId}`;

    try {
      let response = await axios.get(apiUrl);
      this.time = response.data.time * 60;
      this.questions = response.data.questions;
    } catch (err) {
      console.log(err);
    }
  },
  methods: {
    countdown() {
      this.time--;
      let minuteTime = parseInt(this.time / 60, 10);
      let secondTime = parseInt(this.time % 60, 10);
      this.displayTime = minuteTime + " minutes " + secondTime + " seconds";
      if (this.time === 0) {
        clearInterval(this.timer);
      }
    },
    async submitQuiz() {
      const apiUrl = "https://spm-flask.herokuapp.com/submitFinalQuiz";
      let grade = this.computeGrade()
      
      const post_data = {
        sectionId: this.sectionId,
        classId: this.classId,
        option: JSON.stringify(this.learner_answers),
        learnerId: localStorage.getItem("userId"),
        grade: grade,
        quizId: this.sectionId
      };

      try {
        let response = await axios.put(apiUrl, post_data);
        console.log(response);
        if (response.status == 201) {
          this.$router.push({
            path: "/LearnerViewQuizExplanation/",
            query: {
              courseName: this.courseName,
              sectionId: this.sectionId,
              classId: this.classId,
            },
          });
        }
      } catch (err) {
        console.log(err);
      }
    },
    computeGrade(){
      const learner_answers = this.learner_answers
      const answer_list = this.answer_list
      let marks = 0;
      for(let i=0; i<learner_answers.length;i++){
        if (learner_answers[i] == answer_list[i]){
          marks++
        }
      }
      return marks / answer_list.length
    }
  },
  computed: {
    learner_answers() {
      return this.questions.map((item) => item.value);
    },
    answer_list() {
      return this.questions.map((item) => item.answer);
    },
  },
  beforeDestroy() {
    clearInterval(this.timer);
  },
};
</script>
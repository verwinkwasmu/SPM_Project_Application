<template>
  <div id="axiosForm">
    <LearnerHeader />
    <section id="team" class="team section-bg">
      <div class="" data-aos="fade-up">
        <div id="App" class="container">
          <div class="section-title">
            <h2>{{ courseName }}</h2>
            <h3>{{sectionId }} Quiz Answers</h3>
          </div>

          <div v-if="FinalQuiz">
            <div v-if="learnerScore >= 0.85">
              <h4 style="color: green; text-align: center">
                Congratulations you have completed the course!
              </h4>
              <b-modal ref="my-modal" hide-footer title="You passed the quiz!">
                <div class="d-block text-center">
                  <h3>Congratulations!</h3>
                  <p>Woohoo! You have completed this course!</p>
                  <div class="col-lg-12 badge">
                    <img
                      src="~/assets/img/badge.png"
                      class="img-fluid animated"
                      alt=""
                      width="200px"
                      length="200px"
                    />
                  </div>
                </div>
                <b-button
                  class="mt-2"
                  variant="outline-success"
                  block
                  href="LearnerViewCourse"
                  >View other available courses</b-button
                >
                <b-button
                  class="mt-3"
                  variant="outline-secondary"
                  block
                  @click="hideModal"
                  >Continue seeing results</b-button
                >
              </b-modal>
            </div>
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
                    :checked="question.option[0] == question.value"
                    :disabled="question.option[0] != question.value"
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
                    :checked="question.option[1] == question.value"
                    :disabled="question.option[1] != question.value"
                  />
                  {{ question.option[1] }}</label
                >
              </div>

              <div class="option" v-if="question.option[2] != ''">
                <label id="quizrbtn"
                  ><input
                    type="radio"
                    :value="question.option[2]"
                    :name="question.questionId"
                    :checked="question.option[2] == question.value"
                    :disabled="question.option[2] != question.value"
                  />
                  {{ question.option[2] }}</label
                >
              </div>

              <div class="option" v-if="question.option[3] != ''">
                <label id="quizrbtn"
                  ><input
                    type="radio"
                    :value="question.option[3]"
                    :name="question.questionId"
                    :checked="question.option[3] == question.value"
                    :disabled="question.option[3] != question.value"
                  />
                  {{ question.option[3] }}</label
                >
              </div>
            </div>

            <div
              style="margin-left: 25px"
              v-if="question.value != question.answer"
            >
              <p style="color: red">
                Your answer is incorrect. The correct answer is {{question.answer}}.
                <br>
                <b>Reason: {{question.explanation}}</b>
              </p>
            </div>
            <div
              style="margin-left: 25px"
              v-else
            >
              <p style="color: green">Your answer is correct. <br> <b>Reason: {{question.explanation}}</b></p>
            </div>
            <hr />
          </div>

          <!-- <div class="form-group" id="submitquiz">
                          <b-button>Back to Sections</b-button>
                        </div> -->
          <div v-if="FinalQuiz">
            <div v-if="learnerScore >= 0.85" style="text-align: center">
              <b-button href="LearnerViewCourse"
                >View other available courses</b-button
              >
            </div>
            <div v-if="learnerScore <= 0.85" style="text-align: center">
              <h4 style="text-align: center; color: red; padding-bottom: 10px">
                Please reattempt the quiz and study if u r gay
              </h4>
              <b-button
                type="button"
                class="btn btn-secondary"
                href="LearnerTakeFinalQuiz"
                >Redo Quiz</b-button
              >
            </div>
          </div>
          <div v-else style="text-align: center">
            <b-button>Back to Sections</b-button>
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
    displayTime: "",
    msgBox: "",
    learnerAnswer: "Yes",
    CorrectAnswer: "No",
    FinalQuiz: false,
    learnerScore: 0.95,
    classId: "",
    sectionId: '',
    learner_answers: '',
    questions: [],
  }),

  methods: {
    showModal() {
      this.$refs["my-modal"].show();
    },
    hideModal() {
      this.$refs["my-modal"].hide();
    },
  },
  async mounted() {
    this.courseName = this.$route.query.courseName;
    this.sectionId = this.$route.query.sectionId;
    this.classId = this.$route.query.classId;
    this.learner_answers = JSON.parse(localStorage.getItem('learner_answers'))

    const apiUrl = `http://localhost:5003/quiz/${this.classId}/${this.sectionId}`
    try{
      let response = await axios.get(apiUrl)
      this.questions = response.data.questions
      const questions = this.questions

      for (let i=0; i<questions.length; i++){
        questions[i]['value'] = this.learner_answers[i]
      }

      
    }catch(err){
      console.log(err)
    }
    if (this.FinalQuiz && this.learnerScore >= 0.85) {
      this.showModal();
    }
  }
};
</script>
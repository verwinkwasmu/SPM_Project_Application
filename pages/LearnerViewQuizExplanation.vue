<template>
  <div id="axiosForm">
    <LearnerHeader />
    <BadgeModal/>
    <section id="team" class="team section-bg">
      <div class="" data-aos="fade-up">
        <div id="App" class="container">
          <div class="section-title">
            <h2>{{ courseName }}</h2>
            <h3>{{ sectionId }} - Quiz Answers</h3>
          </div>

          <div v-if="sectionId == 'Final Quiz'">
            <div v-if="learnerGrade == 'Pass'">
              <h4 style="color: green; text-align: center">
                Congratulations you have completed the course!
              </h4>
              
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
                Your answer is incorrect. The correct answer is
                {{ question.answer }}.
                <br />
                <b>Reason: {{ question.explanation }}</b>
              </p>
            </div>
            <div style="margin-left: 25px" v-else>
              <p style="color: green">
                Your answer is correct. <br />
                <b>Reason: {{ question.explanation }}</b>
              </p>
            </div>
            <hr />
          </div>

          <div v-if="sectionId == 'Final Quiz'">
            <div v-if="learnerGrade == 'Pass'" style="text-align: center">
              <b-button href="LearnerViewCourse"
                >View other available courses</b-button
              >
            </div>
            <div v-if="learnerGrade == 'Fail'" style="text-align: center">
              <h4 style="text-align: center; color: red; padding-bottom: 10px">
                Please reattempt the quiz and study
              </h4>
              <router-link
                :to="{
                  path: '/LearnerTakeFinalQuiz',
                  query: {
                    sectionId: 'Final Quiz',
                    classId: classId,
                    courseName: courseName,
                  },
                }"
                type="button"
                class="btn btn-secondary"
                >Redo Quiz</router-link
              >
            </div>
          </div>
          <div v-else style="text-align: center">
            <h4 style="text-align: center; color: green; padding-bottom: 10px">
              You have completed this section, please proceed to the next
              section!
            </h4>
            <router-link
              class="btn btn-secondary"
              :to="{
                path: '/LearnerViewSections',
                query: {
                  courseName: this.courseName,
                  sectionName: this.sectionId,
                  classId: this.classId,
                },
              }"
              >View Next Section</router-link
            >
          </div>
        </div>

        <br />
        <br />
      </div>

      <div style="text-align: center">
        <router-link
          class="btn btn-secondary"
          :to="{
            path: '/LearnerViewSections',
            query: {
              courseName: this.courseName,
              sectionName: 'Section 1',
              classId: this.classId,
            },
          }"
          >Back to Sections</router-link
        >
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
    learnerGrade: "",
    classId: "",
    sectionId: "",
    learner_answers: "",
    questions: [],
  }),

  async mounted() {
    this.courseName = this.$route.query.courseName;
    this.sectionId = this.$route.query.sectionId;
    this.classId = this.$route.query.classId;

    const apiUrl1 = `https://spm-flask.herokuapp.com/quiz/${this.classId}/${this.sectionId}`;
    const apiUrl2 = "https://spm-flask.herokuapp.com/retrieveLearnerQuizAnswers";

    const post_data = {
      sectionId: this.sectionId,
      classId: this.classId,
      learnerId: localStorage.getItem("userId"),
    };
    try {
      let response1 = await axios.get(apiUrl1);
      let response2 = await axios.post(apiUrl2, post_data);
      this.questions = response1.data.questions;
      this.learner_answers = JSON.parse(response2.data.data);
      this.learnerGrade = response2.data.grade;

      const questions = this.questions;

      for (let i = 0; i < questions.length; i++) {
        questions[i]["value"] = this.learner_answers[i];
      }
      if(this.learnerGrade == 'Pass'){
        this.$bvModal.show("my-modal");
      }
    } catch (err) {
      console.log(err);
    }
  }
};
</script>
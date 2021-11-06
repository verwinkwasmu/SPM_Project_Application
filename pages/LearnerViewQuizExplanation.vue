<template>
  <div id="axiosForm">
      <LearnerHeader/>
      <section id="team" class="team section-bg">
          <div class="" data-aos="fade-up">
              <div id='App' class="container">
                <div class="section-title">
                  <h2>{{courseName}}</h2>
                  <h3> Section 1 Quiz Answers</h3>
                </div>

                <div v-if="FinalQuiz">
                  <div v-if="learnerScore >= 0.85">
                    <h4 style="color: green; text-align:center;"> Congratulations you have completed the course!</h4>
                      <b-modal ref="my-modal" hide-footer title="You passed the quiz!">
                      <div class="d-block text-center">
                          <h3>Congratulations!</h3>
                          <p>Woohoo! You have completed this course!</p>
                          <div
                              class="col-lg-12 badge"
                          >
                              <img
                              src="~/assets/img/badge.png"
                              class="img-fluid animated"
                              alt=""
                              width='200px'
                              length='200px'
                              />
                          </div>
                      </div>
                       <b-button class="mt-2" variant="outline-success" block href="LearnerViewCourse">View other available courses</b-button>
                       <b-button class="mt-3" variant="outline-secondary" block @click="hideModal">Continue seeing results</b-button>
                      </b-modal>
                  </div>
                </div>

                  <div class="" v-for="(question, index) in questions" :key="index">
                      <h4>{{index+1}}. {{question.fullquestion}}</h4>
                      <br>
                      
                      <div class="optionContainer">
                          <div class="option" >
                              <label id="quizrbtn"><input type="radio" :value="question.option1" name="optradio" v-model="learnerAnswer">    
                              {{question.option1}}</label>
                          </div>

                          <div class="option" >
                              <label id="quizrbtn"><input type="radio" :value="question.option2" name="optradio" v-model="learnerAnswer">     
                              {{question.option2}}</label>
                          </div>
                          
                          <div class="option">
                              <label id="quizrbtn"><input type="radio" :value="question.option3" name="optradio" v-model="learnerAnswer">     
                              {{question.option3}}</label>
                          </div>

                          <div class="option">
                              <label id="quizrbtn"><input type="radio" :value="question.option4" name="optradio" v-model="learnerAnswer">     
                              {{question.option4}}</label>
                          </div>
                      </div>

                      <div style="margin-left: 25px;" v-if="CorrectAnswer != learnerAnswer">
                          <p style="color:red;"> Answer is incorrect. The correct answer is no because u gay.</p>
                      </div>
                      <div style="margin-left: 25px;" v-if="CorrectAnswer == learnerAnswer">
                          <p style="color:green;"> Answer is correct.</p>
                      </div>
                      <hr>
                  </div>

                        <!-- <div class="form-group" id="submitquiz">
                          <b-button>Back to Sections</b-button>
                        </div> -->
                        <div v-if="FinalQuiz">
                          <div v-if="learnerScore >= 0.85" style="text-align: center">
                            <b-button href="LearnerViewCourse">View other available courses</b-button>
                          </div>
                          <div v-if="learnerScore <= 0.85" style="text-align: center">
                            <h4 style="text-align:center; color: red; padding-bottom: 10px;"> Please reattempt the quiz and study if u r gay</h4>
                            <b-button type="button" class="btn btn-secondary" href="LearnerTakeFinalQuiz">Redo Quiz</b-button>
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
  name: "App",
  data: () => ({
    courseName: 'Fundamentals of XXX',
    displayTime: '',
    msgBox: '',
    learnerAnswer: 'Yes',
    CorrectAnswer: 'No',
    FinalQuiz: true,
    learnerScore: 0.55,

    questions: [
      {
        fullquestion: "Are you gay?",
        option1: "Yes",
        option2: "No",
        option3: "Maybe",
        option4: "Maybe not",
      }],

  }),

  methods: {
      showModal() {
        this.$refs['my-modal'].show()
      },
      hideModal() {
        this.$refs['my-modal'].hide()
      }
    },
    mounted() {
      if (this.FinalQuiz && this.learnerScore >= 0.85) 
        {this.showModal();}
    }
};
</script>
<template>
  <div id="axiosForm">
      <TrainerHeader/>
      <section id="team" class="team section-bg">
          <div class="" data-aos="fade-up">
              <div id='App' class="container">
                <div class="section-title">
                  <h2>{{courseName}}</h2>
                  <h3> Section 1 Quiz Answers</h3>
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
                                  <p> Answer is No. Because u gay</p>
                              </div>
                              <div style="margin-left: 25px;" v-if="CorrectAnswer == learnerAnswer">
                                  <p> Answer is correct.</p>
                              </div>
                              <hr>
                        
                          </div>

                        <!-- <div class="form-group" id="submitquiz">
                            <b-button variant="primary" @click="submitQuiz">Submit Quiz</b-button>
                        </div> -->

                        <div class="form-group" id="submitquiz">
                          <b-button>Back to course</b-button>
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

    questions: [
      {
        fullquestion: "Are you gay?",
        option1: "Yes",
        option2: "No",
        option3: "Maybe",
        option4: "Maybe not",
      }],

    learnerAnswer: 'Yes',
    CorrectAnswer: 'Yes',
  }),

    methods: {

      async YesSubmit(event){
        event.preventDefault();
        const apiUrl = "";
      
    },
  
  },
};
</script>
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
                              
                              <div v-if="FinalQuiz">
                                <div v-if="learnerScore <= 0.85">
                                  <p> Please reattempt the quiz and study if u r gay</p>
                                  <!--button to prompt them to redo if they fail or button to see other available if they pass + insert badge -->
                                </div>
                              </div>
                        
                          </div>

                        <div class="form-group" id="submitquiz">
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
    courseName: 'Fundamentals of XXX',
    displayTime: '',
    msgBox: '',
    learnerAnswer: 'Yes',
    CorrectAnswer: 'No',
    FinalQuiz: false,
    learnerScore: 0.65,

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

      
  
  },
};
</script>
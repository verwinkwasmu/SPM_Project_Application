<template>
  <div id="axiosForm">
      <LearnerHeader/>
      <section id="team" class="team section-bg">
          <div class="" data-aos="fade-up">
              <div id='App' class="container">
                <div class="section-title">
                  <h2>{{courseName}}</h2>
                  <h3> Section 1 Quiz </h3>
                </div>
                        <div class="timer">Time Remaining: <strong>{{ displayTime }} </strong></div>

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
                                          <label id="quizrbtn"><input type="radio" :value="question.option3" name="optradio" v-model="learnerAnswer" :class="'is-selected'">     
                                          {{question.option3}}</label>
                                      </div>
      
                                      <div class="option">
                                          <label id="quizrbtn"><input type="radio" :value="question.option4" name="optradio" v-model="learnerAnswer" :class="'is-selected'">     
                                          {{question.option4}}</label>
                                      </div>
                              </div>
                             
                              <hr>
                        
                          </div>

                        <!-- <div class="form-group" id="submitquiz">
                            <b-button variant="primary" @click="submitQuiz">Submit Quiz</b-button>
                        </div> -->

                        <div class="form-group" id="submitquiz">
                          <b-button variant="primary" @click="$bvModal.show('modal-scoped')">Submit Quiz</b-button>
                            <b-modal id="modal-scoped">
                              <template #modal-header="{}">
                                <h5>Submit Quiz</h5>
                              </template>
                              <template #default="{}">
                                <p>Do you want to submit your quiz?</p>
                              </template>
                              <template #modal-footer="{ hide, YesSubmit }">
                                <b-button size="sm" variant="danger" @click="hide('forget')">
                                  No
                                </b-button>
                                <b-button size="sm" variant="success" @click="YesSubmit()">
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
    courseName: 'Fundamentals of XXX',
    time: 1800,
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

    learnerAnswer: ''
  }),

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


      async YesSubmit(event){
        event.preventDefault();
        const apiUrl = "";
      
    },
  
  },

  mounted() {
      this.timer = setInterval(this.countdown, 1000);
    },
  beforeDestroy() {
      clearInterval(this.timer);
    },

  

};
</script>
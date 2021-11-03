<template>
  <div id="axiosForm">
      <TrainerHeader/>
      <section id="team" class="team section-bg">
          <div class="" data-aos="fade-up">
              <div id='App' class="container">
                <div class="section-title">
                  <!-- <h2>{{courseName}}</h2> -->
                  <h2>{{courseName}}</h2>
                  <h3> Section 1 Quiz </h3>
                </div>
                        <div class="timer">Time Remaining: <strong>{{ displayTime }} </strong></div>

                          <div class="" v-for="(question, index) in questions" :key="index">
                              <h4>{{index+1}}. {{question.fullquestion}}</h4>
                              <br>
                              
                              <div class="optionContainer">
                                      <div class="option">
                                          <label id="quizrbtn"><input type="radio" name="optradio">    
                                          {{question.option1}}</label>
                                      </div>
      
                                      <div class="option">
                                          <label id="quizrbtn"><input type="radio" name="optradio" >     
                                          {{question.option2}}</label>
                                      </div>
                                      
                                      <div class="option">
                                          <label id="quizrbtn"><input type="radio" name="optradio" :class="'is-selected'">     
                                          {{question.option3}}</label>
                                      </div>
      
                                      <div class="option">
                                          <label id="quizrbtn"><input type="radio" name="optradio" :class="'is-selected'">     
                                          {{question.option4}}</label>
                                      </div>


                                    
                              </div>
                              <hr>
                          </div>
                  <!-- </div>
              </div>    -->
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
    success: false,
    error: false,
    loading: false,
    error: null,
    courseName: 'Fundamentals of XXX',
    time: 1800,
    displayTime: '',

    questions: [
      {
        fullquestion: "Hi please answer the question",
        option1: "Yes",
        option2: "No",
        option3: "Maybe",
        option4: "Maybe not",
      }],
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
  },

  mounted() {
      this.timer = setInterval(this.countdown, 1000);
    },

  beforeDestroy() {
      clearInterval(this.timer);

    },

};
</script>
<template>
  <div id="axiosForm">
      <TrainerHeader/>
      <section id="team" class="team section-bg">
          <div class="" data-aos="fade-up">
              <div id='App' class="container" data-aos="fade-up">
                <div class="section-title">
                  <!-- <h2>{{courseName}}</h2> -->
                  <h2>{{courseName}}</h2>
                  <h3> Section 1 Quiz </h3>
                </div>
                  
                          <div class="" v-for="(question, index) in questions" :key="index">
                              <h4>{{question.fullquestion}}</h4>
                              <div class="radio">
                                      <div class="radio">
                                          <label id="quizrbtn"><input type="radio" name="optradio" checked>{{question.option1}}</label>
                                      </div>
      
                                      <div class="radio">
                                          <label id="quizrbtn"><input type="radio" name="optradio">{{question.option2}}</label>
                                      </div>
                                      
                                      <div class="radio">
                                          <label id="quizrbtn"><input type="radio" name="optradio">{{question.option3}}</label>
                                      </div>
      
                                      <div class="radio">
                                          <label id="quizrbtn"><input type="radio" name="optradio">{{question.option4}}</label>
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
    // data: null,

    questions: [
      {
        fullquestion: "Hi please answer the question",
        option1: "Yes",
        option2: "No",
        option3: "Maybe",
        option4: "Maybe not",
      }],
        

  }),
  };
</script>
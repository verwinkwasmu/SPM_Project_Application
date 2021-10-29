<template>
    <div>
        <TrainerHeader/>
        <section id="team" class="team section-bg">
            <div class="" data-aos="fade-up">
                <div class="section-title">
                    <h2>Fundamentals of Xerox WorkCentre 7845 Final Quiz</h2>
                    <h1>Final Quiz questions</h1>
                    Assume 1 correct answer is 1 mark
                </div>

                <div id="app" class="container">
                    <form>
                        
                        <div class="work-questions">
                            <div class="form-row" v-for="(question, index) in questions" :key="index">
                              <div class="form-group col-md-10">
                                  <label>Question: </label>
                                  <input v-model="question.fullquestion" :name="`questions[${index}][fullquestion]`" type="text" class="form-control" placeholder="Enter your question here">
                              </div>
                              <div class="form-group col-md-7">
                                  <label>Option 1: </label>
                                  <input v-model="question.option1" :name="`questions[${index}][option1]`" type="text" class="form-control" placeholder="Option 1">
                              </div>
                              <div class="form-group col-md-7">
                                  <label>Option 2: </label>
                                  <input v-model="question.option2" :name="`questions[${index}][option2]`" type="text" class="form-control" placeholder="Option 2">
                              </div>
                              <div class="form-group col-md-7">
                                  <label>Option 3: </label>
                                  <input v-model="question.option3" :name="`questions[${index}][option3]`" type="text" class="form-control" placeholder="Option 3">
                              </div>
                              <div class="form-group col-md-7">
                                  <label>Option 4: </label>
                                  <input v-model="question.option4" :name="`questions[${index}][option4]`" type="text" class="form-control" placeholder="Option 4">
                              </div>

                              <div class="form-group col-md-7">
                                  <label>Answer: </label>
                                  <b-select v-model="question.answer">
                                    <option disabled value="">Please select one</option>
                                      <option>Option 1</option>
                                      <option>Option 2</option>
                                      <option>Option 3</option>
                                      <option>Option 4</option>
                                  </b-select>
                              </div>
                              
                               <div class="form-group col-md-10">
                                  <label>Explanation for answer: </label>
                                  <input v-model="question.explanation" :name="`questions[${index}][explanation]`" type="text" class="form-control" placeholder="Input explanation">
                              </div>
                              
                              <div class="form-group col-md-12">
                                  <hr>
                              </div>

                            
                            </div>
                        </div>

                        <div class="form-group">
                            <button @click="addquestion" type="button" class="btn btn-primary">Add Question</button>
                        </div>
                        <div class="form-group">
                            <button @click="removequestion" type="button" class="btn btn-danger">Remove Question</button>
                        </div> 
                        <br>
                        <div class="form-group">
                            <label>Quiz Duration (in minutes): </label>
                            <div style="padding-right: 1090px">
                              <input type='number' v-model="quizTimer" min=1 max=60 class="form-control">
                            </div>
                        </div>
                    </form>
                  <br>

                  </div>
                    <div class="buttongroup">
                      <div class="TrainerCreateQuiz">
                          <button @click="submit" type="button" class="TrainerCreateQuiz-btn">Create Quiz</button>
                          <!-- <span class="spinner-border spinner-border-sm" role="status" aria-hidden="true"></span>
                          Loading... -->
                      </div>

                      <div class="cancel">
                          <a href="TrainerViewSection" class="cancel-btn">Cancel</a>
                      </div>

                              
                      </div>
                  </div>
        </section>
    </div>
</template>

<script>
export default {
  
  name: "App",
  // components: {
  //   VueLoadingButton,
  // },
  
  data: () => ({
    questions: [
      {
        fullquestion: "",
        option1: "",
        option2: "",
        option3: "",
        option4: "",
        answer: "",
        explanation: "",
        quizTimer: ""
        
      },
    ]
  }),

  methods: {
    addquestion () {
      this.questions.push({
        fullquestion: '',
        option1: '',
        option2: '',
        option3: '',
        option4: '',

      })
    },

     removequestion (){
        this.questions.pop({
            fullquestion: '',
            option1: '',
            option2: '',
            option3: '',
            option4: '',
        })
    },

    submit () {
      const data = {
        questions: this.questions
      }
      alert(JSON.stringify(data, null, 2))
    },
  }
};
</script>

<style>
.example {
  font-family: "Avenir", Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  margin-top: 60px;
  text-align: center;
}
</style>
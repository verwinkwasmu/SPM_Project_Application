<template>
    <div id="axiosForm">
        <TrainerHeader/>
        <section id="team" class="team section-bg">
            <div class="" data-aos="fade-up">
                <div class="section-title">
                    <h2>Fundamentals of Xerox WorkCentre 7845 Quiz</h2>
                    <h1>Quiz questions</h1>
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

                        <div class="form-group" id="addquestion">
                            <button @click="addquestion" type="button" class="btn btn-primary">Add Question</button>
                        </div>
                         <div class="form-group" id="removequestion">
                            <button @click="removequestion" type="button" class="btn btn-danger">Remove Question</button>
                        </div> 
                        <br>
                        <div class="form-group">
                            <label>Quiz Duration (in minutes): </label>
                            <div style="padding-right: 1005px">
                              <input type='number' v-model="quizTimer" min=1 max=60 class="form-control">
                            </div>
                        </div>
                    </form>
                  <br>

                   <div class="loader" v-if="loading">
                      <img class="loaderImg" src="assets/img/ajax-loader.gif">
                  </div>

                  
                  </div>
                    <div class="buttongroup">
                      <div class="TrainerCreateQuiz">
                          <a @click="submit" class="TrainerCreateQuiz-btn">
                            Create Quiz</a>
                      </div>

                      <div class="cancel">
                        <a href="TrainerViewSection" class="cancel-btn">Cancel</a>
                      </div>

                      <div
                        v-if="success"
                        class="alert alert-success alert-dismissible fade show"
                        role="alert"
                      >
                        {{ message }}
                        <button
                          type="button"
                          class="btn-close"
                          data-bs-dismiss="alert"
                          aria-label="Close"
                        ></button>
                      </div>


                      <div
                        v-if="error"
                        class="alert alert-danger alert-dismissible fade show"
                        role="alert"
                      >
                        {{ message }}
                        <button
                          type="button"
                          class="btn-close"
                          data-bs-dismiss="alert"
                          aria-label="Close"
                        ></button>
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
    success: false,
    error: false,
    loading: false,
    error: null,
    // data: null,

    questions: [
      {
        fullquestion: "",
        option1: "",
        option2: "",
        option3: "",
        option4: "",
        answer: "",
        explanation: "",
      }],
    
    quizTimer: '',
    

  }),

  methods: {
    addquestion () {
      this.questions.push({
        fullquestion: '',
        option1: '',
        option2: '',
        option3: '',
        option4: '',
        answer: '',
        explanation: ''
      })
    },

    removequestion (){
      this.questions.pop({
          fullquestion: '',
          option1: '',
          option2: '',
          option3: '',
          option4: '',
          answer: '',
          explanation: ''
        })
    },

    submit() {
      if(!this.questions || !this.quizTimer){
        this.error = true
        this.message = "Please make sure Question, Options, Answer, Explanation and Quiz Duration are not empty!"
        return
      }
      const formData = {
        questions: this.questions,
        quizTimer: this.quizTimer
      };
      try{
        this.loading = true
        axios.post("https://jsonplaceholder.typicode.com/posts", formData)
        .then(response => {
            this.reset();
            this.success = true;
            this.message = "Quiz successfully created! 😃"
            console.log('yay')
        })
      }catch(error){
        this.error = true;
        console.log(error)
      }
      
    },

    reset(){
        this.loading= false
        this.success = false;
        this.error = false;    
    }
  }
};
</script>

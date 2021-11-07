<template>
    <div id="axiosForm">
        <TrainerHeader/>
        <section id="team" class="team section-bg">
            <div class="" data-aos="fade-up">
                <div class="section-title">
                    <h2>{{classObj.classId}}</h2>
                    <h1>Final Quiz questions</h1>
                    Assume 1 question is 1 mark
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
                                      <option v-if="question.option1!=''">{{question.option1}}</option>
                                      <option v-if="question.option2!=''">{{question.option2}}</option>
                                      <option v-if="question.option3!=''">{{question.option3}}</option>
                                      <option v-if="question.option4!=''">{{question.option4}}</option>
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
                         <router-link :to="{path: '/TrainerViewSection', query: {classId: classObj.classId}}" class="cancel-btn">Cancel</router-link>
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
    classObj: {},
    sectionId:"Final Quiz",
    quizId: "Final Quiz",
    course: {},
    courseId: localStorage.getItem('courseId'),
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
    quizexist: false,
    questionNum: 1,

  }),
  async mounted() {
    const apiUrl1 = `http://localhost:5002/getCourse/${this.courseId}`;
    const apiUrl2 = `http://localhost:5002/getClass/${this.$route.query.classId}`;
    try {
      let response1 = await axios.get(apiUrl1);
      let response2 = await axios.get(apiUrl2);

      this.course = await response1.data;
      console.log(this.course);
      this.classObj = await response2.data;
      console.log(this.classObj);

      this.error = false;
    } catch (err) {
      console.log(err);
      this.error = true;
      this.message = err;
    }
  },

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

    reset(){
        this.loading= false
        this.success = false;
        this.error = false;    
    }, 

    async submit(event) {
      event.preventDefault();
      // form validation
      if(!this.questions || !this.quizTimer){
        this.error = true
        this.message = "Please make sure Question, Options, Answer, Explanation and Quiz Duration are not empty!"
        return
      }

      // create section
      await this.createSection(event);

      // create quiz
      await this.createQuiz(event);

      // create questions
      for (let i = 0; i<this.questions.length; i++){
        console.log(this.questions[i]);
        await this.createQuestion(event, this.questions[i], this.questionNum);
        this.questionNum++;
      }

      if (!this.error){
        setTimeout(function(){ 
          this.$router.push({path: '/TrainerViewSection', query: {classId: this.classObj.classId}});
        }.bind(this), 1000);
      }
     
    },
    
    async createSection(event) {
      event.preventDefault();
      
      const apiUrl = "http://localhost:5002/createSection";
      const section_details = {
        sectionId: this.sectionId,
        classId: this.classObj.classId,
        fileName: ""
      };
      console.log(this.sectionId);
      console.log(this.classObj.classId);
      try{
        let response = await axios.post(apiUrl, section_details)
        console.log(response)
        if (response.status == 201) {
              this.data = response.data;
              this.error = false;
              this.message = "Section Successfully Created! 😃";
            } else {
              this.error = true;
              this.message = "Section already exists!";
            }
      }catch(err){
        console.log(err)
        this.error = true;
        this.message = err
      }
    },

    async createQuiz(event){
      event.preventDefault();
      const apiUrl = "http://localhost:5003/createQuiz";
      const quiz_details = {
        sectionId: this.sectionId,
        classId: this.classObj.classId,
        quizId: this.quizId,
        time: this.quizTimer
      };
      this.loading = true
      try{
        let response = await axios.post(apiUrl, quiz_details)
        console.log(response)
        if (response.status == 201) {
          this.reset();
          this.data = response.data;
          // alert("Quiz Successfully Created! 😃");
        } else {
          this.error = true;
          alert("Quiz already exists!");
        }
      }catch(err){
        console.log(err)
        this.error = true;
        this.message = err
      }
    },


    async createQuestion(event, qn, number){
      event.preventDefault();
      const apiUrl = "http://localhost:5003/createQuestion";
      var option = "";
      if (qn.option1 != ""){
        option += qn.option1 + ";";
      }
      if (qn.option2 != ""){
        option += qn.option2 + ";";
      }
      if (qn.option3 != ""){
        option += qn.option3 + ";";
      }
      if (qn.option4 != ""){
        option += qn.option4;
      }
      else{
        option = option.slice(0,-1);
      }
      
      const question_details = {
        sectionId : this.sectionId,
        classId : this.classObj.classId,
        quizId : this.quizId,
        questionId : "Question " + number.toString(),
        question : qn.fullquestion,
        option : option,
        answer : qn.answer,
        explanation : qn.explanation
      };
      this.loading = true
      try{
        let response = await axios.post(apiUrl, question_details)
        console.log(response)
        if (response.status == 201) {
          this.reset();
          this.success = true;
          this.message = "Questions successfully created! 😃"
          console.log(response.status)
          this.error = false;
        } else {
          this.error = true;
          alert("Question already exists!");
        }
      }catch(err){
        console.log(err)
        this.error = true;
        this.message = err
      }
    },
  }
};
</script>

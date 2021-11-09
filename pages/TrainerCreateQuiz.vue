<template>
    <div id="axiosForm">
        <TrainerHeader/>
        <section id="team" class="team section-bg">
            <div class="" data-aos="fade-up">
                <div class="section-title">
                    <h2>{{course.courseName}}</h2>
                    <h1>{{this.quizId}} questions</h1>
                </div>

                <div id="app" class="container">
                    <form>
                        
                        <div class="work-questions">
                            <div class="form-group" v-for="(question, index) in questions" :key="index">
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
                                      <option>{{question.option1}}</option>
                                      <option>{{question.option2}}</option>
                                      <option>{{question.option3}}</option>
                                      <option>{{question.option4}}</option>
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
                        <div v-if="quizExist==false" class="form-group">
                            <label>Quiz Duration (in minutes): </label>
                            <div style="padding-right: 1005px">
                              <input type='number' v-model="quizTimer" min=1 max=60 class="form-control">
                            </div>
                        </div>
                    </form>
                  <br>

                   <div class="loader" v-if="loading">
                      <img class="loaderImg" src="/assets/img/ajax-loader.gif">
                  </div>

                  
                  </div>
                    <div class="buttongroup" style="margin-left: 45%">
                      <div class="TrainerCreateQuiz">
                          <a @click="submit" class="btn btn-success">
                            Create Quiz</a>
                      </div>

                      <div class="cancel">
                        <router-link :to="{path: '/TrainerQuizList/', query: {sectionId: sectionId, classId: classObj.classId}}"  class="btn btn-danger">Cancel</router-link>
                      </div>
            
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
    sectionId:"",
    quizId: "",
    course: {},
    

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
    quizExist: false,
    courseId: localStorage.getItem('courseId'),
    questionNum: 1
  }),
  async mounted() {
    const apiUrl1 = `https://spm-flask.herokuapp.com/getCourse/${this.courseId}`;
    const apiUrl2 = `https://spm-flask.herokuapp.com/getClass/${this.$route.query.classId}`;
    const apiUrl3 = `https://spm-flask.herokuapp.com/quiz/${this.$route.query.classId}/${this.$route.query.sectionId}`;
    try {
      let response1 = await axios.get(apiUrl1);
      let response2 = await axios.get(apiUrl2);
      let response3 = await axios.get(apiUrl3);

      if (response3.status == 200){
        this.quizExist = true;
        this.questionNum = await response3.data.questions.length + 1;
      }

      this.course = await response1.data;
      this.classObj = await response2.data;
      this.sectionId = await this.$route.query.sectionId;
  
      this.quizId = await this.sectionId.replace("Section", "Quiz");

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

    async submit(event) {
      event.preventDefault();
      // form validation
      if(!this.questions || (!this.quizTimer&&!this.quizExist)){
        this.error = true
        this.message = "Please make sure Question, Options, Answer, Explanation and Quiz Duration are not empty!"
        return
      }

      // create quiz
      if (!this.quizExist){
        await this.createQuiz(event);
      }

      // create questions
      for (let i = 0; i<this.questions.length; i++){
        console.log(this.questions[i]);
        await this.createQuestion(event, this.questions[i], this.questionNum);
        this.questionNum++;
      }

      if (!this.error){
        setTimeout(function(){ 
          this.$router.push({path: '/TrainerViewSection/', query: {sectionId: this.sectionId, classId: this.classObj.classId}});
        }.bind(this), 1000);
      }
     
    },

    async createQuiz(event){
      event.preventDefault();
      const apiUrl = "https://spm-flask.herokuapp.com/createQuiz";
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
      const apiUrl = "https://spm-flask.herokuapp.com/createQuestion";
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

    reset(){
        this.loading= false
        this.success = false;
        this.error = false;    
    }
  }
};
</script>

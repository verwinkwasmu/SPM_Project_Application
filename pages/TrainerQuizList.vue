<template>
    <div>
        <TrainerHeader/>

        <section id="team" class="team section-bg">
            <div class="container" data-aos="fade-up">
                <div class="row pb-5 mb-2 ml-0">
                    <div class="viewClass">
                        <router-link :to="{path: '/TrainerViewSection/', query: {classId: classObj.classId}}" class="btn btn-primary">Back to see all Classes</router-link>
                    </div>
                </div>
                <div class="section-title">
                  
                    <h2>{{sectionId}}</h2>
                    <h3>{{classObj.classId}}</h3>
                    <div class="row pt-3">
                      <div class="col-lg-6" id="TrainerViewCourseDetails" style="padding-bottom: 40px">
                          <div class="member d-flex"
                                    data-aos="zoom-in"
                                    data-aos-delay="100">      
                              <div v-if="quizExist==true" class="member-info mx-auto">
                                <h4>{{ quiz.quizId }}</h4> 
                                <br>
                                <h4>Quiz Time: {{quiz.time}}mins</h4>
                              </div>
                              <div v-else class="member-info mx-auto">
                                <h4 class="text-danger">No Quiz Created yet</h4> 
                              </div>
                          </div>
                        </div>
                    </div>


                    <div class="TrainerCreateSection">
                        <router-link :to="{path: '/TrainerCreateQuiz/', query: {sectionId: sectionId, classId: classObj.classId}}"  class="btn btn-success">
                        <span v-if="quizExist==false">Create Quiz</span>
                        <span v-else>Add Questions</span>
                        </router-link>
                    </div>

                </div >
                   
                  <table v-if="quizExist==true" class="table">
                    <thead>
                        <tr>
                        <th scope="col">Question</th>
                        <th scope="col">Option 1</th>
                        <th scope="col">Option 2</th>
                        <th scope="col">Option 3</th>
                        <th scope="col">Option 4</th>
                        <th scope="col">Answer</th>
                        <th scope="col">Explanation</th>
                        <th></th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr v-for="question in questions" :key="question.questionId">
                          <td>{{question.question}}</td>
                          <td v-for="option in question.option" :key="option">
                            {{option}}
                          </td>
                          <td>{{question.answer}}</td>
                          <td>{{question.explanation}}</td>
                          <td>
                            <div class="form-group" id="removequestion">
                              <button @click="removeQn(question.questionId)" type="button" class="btn btn-danger">Remove</button>
                            </div> 
                          </td>
                        </tr>
                    </tbody>
                </table>
            </div>

        </section>
    </div>
</template>

<script>
import axios from "axios";

export default {
  data: () => ({
    course: {},
    sectionId: "",
    classObj: {},
    error: false,
    message: "",
    enrolment: {},
    quiz:{},
    questions: [],
    quizExist: false,
    courseId: localStorage.getItem('courseId')
  }),
  async mounted() {
    const apiUrl1 = `https://spm-flask.herokuapp.com/getCourse/${this.courseId}`;
    const apiUrl2 = `https://spm-flask.herokuapp.com/getClass/${this.$route.query.classId}`;
    const apiUrl3 = `https://spm-flask.herokuapp.com/quiz/${this.$route.query.classId}/${this.$route.query.sectionId}`;
    
    let response1 = await axios.get(apiUrl1);
    let response2 = await axios.get(apiUrl2);
    let response3 = await axios.get(apiUrl3);

    console.log(response3.data);
    if (response3.status == 200){
      this.quiz = await response3.data.quiz;
      this.questions = await response3.data.questions;
      console.log(this.questions);
      this.quizExist = true;
    }

    this.course = await response1.data;
    this.classObj = await response2.data;
    this.sectionId = await this.$route.query.sectionId;

    console.log(this.classObj);
    console.log(this.course);
    console.log(this.sectionId);
    

    this.error = false;
    
  },
  methods:{
    async removeQn(questionId){
      const apiUrl = `https://spm-flask.herokuapp.com/removeQuestion`;
      const data = {
        sectionId: this.sectionId,
        classId: this.classObj.classId,
        quizId: this.quiz.quizId,
        questionId: questionId
      };
      try {
        let response = await axios.delete(apiUrl, { data: data });
        if (response.status == 200){
          alert(response.data.message);
          window.location.reload(true);
        }
        else{
          alert("Please Try again!");
        }

        this.error = false;
      } catch (err) {
        console.log(err);
        this.error = true;
        this.message = err;
      }
    }
  },

};
</script>
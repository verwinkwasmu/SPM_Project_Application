<template>
    <div>
        <TrainerHeader/>

        <section id="team" class="team section-bg">
            <div class="container" data-aos="fade-up">
                <div class="row pb-5 mb-2 ml-0">
                    <div class="viewClass">
                        <router-link :to="{path: '/TrainerViewSection', query: {classId: classObj.classId}}" class="viewClass-btn">Back to see all Classes</router-link>
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
                        <router-link :to="{path: '/TrainerCreateQuiz', query: {sectionId: sectionId, classId: classObj.classId}}"  class="TrainerCreateSection-btn">
                        <span v-if="quizExist==false">Create Quiz</span>
                        <span v-else>Add Questions</span>
                        </router-link>
                    </div>

                </div>
                   
                  <table class="table">
                    <thead>
                        <tr>
                        <th scope="col">#</th>
                        <th scope="col">Question</th>
                        <th scope="col">Option 1</th>
                        <th scope="col">Option 2</th>
                        <th scope="col">Option 3</th>
                        <th scope="col">Option 4</th>
                        <th scope="col">Answer</th>
                        <th scope="col">Explanation</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr v-for="question in questions" :key="question.questionId">
                          <td>{{question.questionId}}</td>
                          <td>{{question.question}}</td>
                          <td>{{question.option[0]}}</td>
                          <td>{{question.option[1]}}</td>
                          <td>{{question.option[2]}}</td>
                          <td>{{question.option[3]}}</td>
                          <td>{{question.answer}}</td>
                          <td>{{question.explanation}}</td>
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
    const apiUrl1 = `http://localhost:5002/getCourse/${this.courseId}`;
    const apiUrl2 = `http://localhost:5002/getClass/${this.$route.query.classId}`;
    const apiUrl3 = `http://localhost:5003/quiz/${this.$route.query.classId}/${this.$route.query.sectionId}`;
    try {
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
    } catch (err) {
      console.log(err);
      this.error = true;
      this.message = err;
    }
  },

};
</script>
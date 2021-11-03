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
                  
                    <h2>{{course.courseName}}</h2>
                    <div class="TrainerCreateSection">
                        <router-link :to="{path: '/TrainerCreateQuiz', query: {sectionId: sectionId, classId: classObj.classId}}"  class="TrainerCreateSection-btn">Create Quiz</router-link>
                    </div>

                </div>
                   
                  <table class="table">
                    <thead>
                        <tr>
                        <th scope="col">Current Quizzes</th>
                        <th scope="col">Quiz Type</th>
                        <th scope="col">View Status</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr>
                        <td> Assignment 1</td>  <!-- can click onto it to see the quiz questions--> 
                        <td>Graded</td>
                        <td>Released</td>
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
    courseId: localStorage.getItem('courseId')
  }),
  async mounted() {
    // const apiUrl1 = `http://localhost:5002/viewSections/${this.$route.query.classId}`;
    const apiUrl1 = `http://localhost:5002/getCourse/${this.courseId}`;
    const apiUrl2 = `http://localhost:5002/getClass/${this.$route.query.classId}`;
    try {
      let response1 = await axios.get(apiUrl1);
      let response2 = await axios.get(apiUrl2);

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
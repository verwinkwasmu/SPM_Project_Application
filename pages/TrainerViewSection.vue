<template>
    <div>
        <TrainerHeader/>
        <section id="team" class="team section-bg">
        <div class="container" data-aos="fade-up">

           <div class="row pb-5 mb-2 ml-0">
            <div class="viewClass">
              <router-link :to="{path: '/TrainerViewClasses'}" class="btn btn-primary" >Back to see all Classes</router-link>
            </div>
          </div>

          <div class="section-title">

            <h2>{{classObj.classId}}</h2>
            <h3>{{course.courseName}}</h3>

            <div class="TrainerCreateSection">
              <router-link :to="{path: '/TrainerCreateSection', query: {classId: classObj.classId}}" class="btn btn-success">Create Section</router-link>
            </div>
            <div v-if="finalQuizExist==false" class="TrainerCreateFinalQuiz">
              <router-link :to="{path: '/TrainerCreateFinalQuiz', query: {classId: classObj.classId, classTitle : classObj.classTitle}}" class="btn btn-success">Create Final Quiz</router-link>
            </div>
            
          </div>
              
      
          <div class="row">
            <div class="col-lg-6" v-for="section in sections" :key="section.sectionId">
              <div
                class="member d-flex align-items-start" style="margin-bottom: 20px;"
                data-aos="zoom-in"
                data-aos-delay="100"
              >
                
                <div class="member-info" >
                  <h4>{{section.sectionId}}</h4>
                  <p>
                    Explicabo voluptatem mollitia et repellat qui dolorum quasi
                  </p>
                  
                </div>
                <div class="editSection">  
                    <router-link :to="{path: '/TrainerCourseMaterials', query: {classTitle : classObj.classTitle, sectionId: section.sectionId, classId: classObj.classId}}" class="btn btn-outline-dark">Course Materials</router-link>
                </div>
                

                <div class="quizList">  
                    <router-link :to="{path: '/TrainerQuizList', query: {classTitle : classObj.classTitle, sectionId: section.sectionId, classId: classObj.classId}}" class="btn btn-outline-dark">Quiz List</router-link>
                </div>

              </div>
            </div>

            

          </div>
        </div>

      </section>
    </div>
</template>


<script>
import axios from "axios";

export default {
  data: () => ({
    course: {},
    sections: [],
    classObj: {},
    error: false,
    message: "",
    enrolment: {},
    courseId: localStorage.getItem('courseId'),
    finalQuizExist: false
  }),
  async mounted() {
    const apiUrl1 = `https://spm-flask.herokuapp.com/viewSections/${this.$route.query.classId}`;
    const apiUrl2 = `https://spm-flask.herokuapp.com/getCourse/${this.courseId}`;
    const apiUrl3 = `https://spm-flask.herokuapp.com/getClass/${this.$route.query.classId}`;
    try {
      let response1 = await axios.get(apiUrl1);
      let response2 = await axios.get(apiUrl2);
      let response3 = await axios.get(apiUrl3);

      this.sections = await response1.data.data;
      this.course = await response2.data;
      this.classObj = await response3.data;
  
      
      for (var i=0; i<this.sections.length; i++){
        
        if (this.sections[i].sectionId == "Final Quiz"){
          this.finalQuizExist = true;
        }
      }

      this.error = false;
    } catch (err) {
      console.log(err);
      this.error = true;
      this.message = err;
    }
  },

};
</script>
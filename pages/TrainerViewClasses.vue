<template>
    <div>
        <TrainerHeader/>
        <section id="team" class="team section-bg">
        <div class="container" data-aos="fade-up">

          <div class="row pb-5 mb-2 ml-0">
            <div class="viewClass">
              <router-link :to="{path: '/TrainerViewCourses', query: {trainerId: 13}}" class="viewClass-btn">Back to see all Courses</router-link>
            </div>
          </div>

          <div class="section-title">
              
            <h2>{{ course.courseName }}</h2>
            <!-- <div class="createClass">
                <a href="TrainerViewSection" class="createClass-btn">View Sections</a>
            </div> -->
          </div>
              
         <div class="row">
                <div class="col-lg-8" id="TrainerViewCourseDetails" style="padding-bottom: 40px">
                     <div class="member d-flex align-items-start"
                              data-aos="zoom-in"
                              data-aos-delay="100"
                            >
                                
                        <div class="member-info">
                          <!-- <h4>{{ course.courseName }}</h4> -->

                          <div v-if="course.prerequisites != ''">
                            <h4>Prequiresite Course:</h4> 
                            <p>{{ course.prerequisites }}</p> <br>
                            <!-- Prerequisite Courses: 

                            <ul>
                              <li>{{ course.prerequisites }}</li>
                            </ul> -->
                          </div>
                          <div v-else>
                            <br/>
                          </div>
                          <h4>Period of Enrollment: </h4> <p>1st July - 30th July</p> <br>
                          <h4>Course Description: </h4>
                          <p>
                              {{course.courseDescription}}
                          </p>
                          </div>
                      </div>
                </div>
          </div>


          <div class="row">
            <div class="col-lg-6 mt-5" v-for="_class in classes" :key="_class.classId">
              <div
                class="member d-flex align-items-start"
                data-aos="zoom-in"
                data-aos-delay="100"
              >
                <div class="member-info">
                  <h4>{{ _class.classTitle }}</h4>
                  <span>{{ _class.trainerName }}</span>
                  <p> Maximum Class Capacity: {{_class.classSize}} </p>
                  <p> Current Class Size: {{ enrolment[_class.classId] }} </p>
                  <br>

                  <p>
                    Start Date: {{_class.startDate}} 
                  </p>
                  <p>
                    Start Time: {{_class.startTime}} 
                  </p>


                  <br>

                  <p>
                    End Date: {{_class.endDate}} 
                  </p>
                  <p>
                    End Time: {{_class.endTime}} 
                  </p>
                </div>
                <div class="viewClass">
                  <router-link :to="{path: '/TrainerViewSection', query: {classId: _class.classId, courseId: _class.courseId}}" class="viewClass-btn">View Sections</router-link>
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
    classes: [],
    error: false,
    message: "",
    enrolment: {}
  }),
  async mounted() {
    const apiUrl1 = `http://localhost:5002/getTrainerClasses/13/${this.$route.query.courseId}`;
    const apiUrl2 = `http://localhost:5002/getCourse/${this.$route.query.courseId}`;
    const getEnrolmentURL = `http://localhost:5004/enrolment/size/13/${this.$route.query.courseId}`;
    try {
      let response1 = await axios.get(apiUrl1);
      let response2 = await axios.get(apiUrl2);
      let response3 = await axios.get(getEnrolmentURL);

      console.log(response1)
      console.log(response2)
      console.log(response3)

      this.classes = await response1.data.data;
      this.course = await response2.data;
      this.enrolment = await response3.data.data;
  
      console.log(this.classes);
      console.log(this.course);
      console.log(this.enrolment);

      this.error = false;
    } catch (err) {
      console.log(err);
      this.error = true;
      this.message = err;
    }
  },

};
</script>
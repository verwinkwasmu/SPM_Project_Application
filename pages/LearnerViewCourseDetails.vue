<template>
    <div>
        <LearnerHeader/>



        <section id="team" class="team section-bg">  <!--box-->
            <div class="container" data-aos="fade-up">

                <div class="section-title">
                    <h2>{{ course.courseName }}<br></h2>
                </div>
                <div class="LearnerEnrolStatus">
                    <span class="badge badge-secondary">Pending Approval</span>
                </div>
                    <div class="row">
                        <div class="col-lg-8" id="createCourse" style="padding-bottom: 100px">
                            <div
                                class="member d-flex align-items-start"
                                data-aos="zoom-in"
                                data-aos-delay="100"
                            >
                                <div class="LearnerEnrol">
                                    <router-link :to="{path: '/LearnerViewClass'}" class="LearnerEnrol-btn" v-if="notEnrolled">Enrol into Course</router-link>
                                </div>
                                <div class="LearnerWithdraw">  
                                    <a href="" class="LearnerWithdraw-btn">Withdraw from Course</a>
                                </div>
                                
                                <div class="member-info">
                                    <!-- <h4>{{ course.courseName }}</h4> -->
                                    <h4>Course ID: </h4> 
                                    <p>{{ course.courseId }}</p> <br>
                                    <h4>Course Description: </h4>
                                        <p>{{course.courseDescription}}</p> <br>
                                    <h4>Prerequisite Courses:</h4>
                                    <ul v-if="course.prerequisites != ''">
                                        <li>{{ course.prerequisites }}</li> 
                                    </ul>
                                    <ul v-else>
                                        <li>No prerequisites required</li>
                                    </ul>
                                </div>
                            </div>

                            <!-- <div class="LearnerWithdraw">  
                                <a href="" class="LearnerWithdraw-btn">Withdraw from Course</a>
                            </div>  -->
                            
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
    error: false,
    message: "",
    enrolment: {},
    courseId: localStorage.getItem('courseId'),
    notEnrolled: true,
    enrolled: false,
  }),
  async mounted() {
    const apiUrl1 = `http://localhost:5002/getCourse/${this.courseId}`;
    try {
      let response1 = await axios.get(apiUrl1);

      console.log(response1)

      this.course = await response1.data;

      console.log(this.course)

      this.error = false;
    } catch (err) {
      console.log(err);
      this.error = true;
      this.message = err;
    }
  },
};
</script>


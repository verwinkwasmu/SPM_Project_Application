<template>
  <div>
    <Header />

    <!--<Homepage/>
       -->

    <section id="team" class="team section-bg">
      <!--box-->
      <div class="container" data-aos="fade-up">
        <div class="section-title">
          <h2>
            {{ course.courseName }} <br />
            <br />
            {{ myClass.classTitle }}
          </h2>
        </div>
        <div class="row">
          <div class="col-lg-8" id="createCourse" style="padding-bottom: 50px">
            <div
              class="member d-flex align-items-start"
              data-aos="zoom-in"
              data-aos-delay="100"
            >
              <div class="member-info">
                <h4>{{ course.courseName }}</h4>
                Prerequisite Courses:
                <ul v-if="course.prerequisites == null">
                    <b>No Prerequisites</b>
                </ul>
                <ul v-else>
                    <li>{{course.prerequisites}}</li>
                </ul>
                <h4>Maximum Class Size:</h4>
                <p>{{ myClass.classSize }}</p>
                <br />
                <h4>Period of Enrollment:</h4>
                <p>{{ myClass.enrolmentPeriod }}</p>
                <br />
                <h4>Period of Class:</h4>
                <p>{{ myClass.startTime}}, {{myClass.startDate}} to {{myClass.endTime}}, {{myClass.endDate}}</p>
                <br />
                <h4>Course Description:</h4>
                <p>
                  {{ course.courseDescription }}
                </p>
              </div>
            </div>
          </div>

          <div class="col-lg-8 mt-4 mt-lg-0" id="createCourse">
            <div class="member-info" style="padding-bottom: 100px">
              <h5>Assign a Trainer:</h5>
              <b-select v-model="selectedTrainer">
                <option
                  v-for="trainer in trainers"
                  :value="trainer"
                  :key="trainer.userId"
                >
                  {{ trainer.userName }}
                </option>
              </b-select>
              <br />
              <div
                v-if="error == true"
                class="alert alert-danger alert-dismissible fade show mt-5"
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
                v-else-if="error == false"
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
              <div class="addEngineer mt-5">
                <a href="" class="addEngineer-btn" @click="assignTrainer"
                  >Assign Trainer</a
                >
              </div>
            </div>

            <!--<section id="team" class="team section-bg">-->
            <!-- <b-tabs>
              <b-tab-item label="Table">
                <b-table
                  :data="data"
                  :columns="columns"
                  :checked-rows.sync="checkedRows"
                  :is-row-checkable="row"
                  checkable
                  :checkbox-position="checkboxPosition"
                > -->
            <!-- <template #bottom-left>
                                                <b>Total checked</b>: {{ checkedRows.length }}
                                            </template> -->
            <!-- </b-table>
              </b-tab-item>

              <div class="remove">
                <a href="EditClass" class="remove-btn">Remove</a>
              </div> -->
            <!-- Link to DB to refresh page with updated list-->

            <!-- <b-tab-item label="Checked rows">
                                        <pre>{{ checkedRows }}</pre>
                                    </b-tab-item> -->
            <!-- </b-tabs> -->
            <!-- </div> -->
            <!--</section>-->
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
    myClass: {},
    trainers: [],
    error: null,
    message: "",
    selectedTrainer: "",
  }),
  mounted() {
    const apiUrl1 = `http://localhost:5002/getCourse/${this.$route.query.courseId}`;
    const apiUrl2 = `http://localhost:5002/getClass/${this.$route.query.classId}`;
    const apiUrl3 = `http://localhost:5001/getTrainers`;

    const requestOne = axios.get(apiUrl1);
    const requestTwo = axios.get(apiUrl2);
    const requestThree = axios.get(apiUrl3);

    axios
      .all([requestOne, requestTwo, requestThree])
      .then(
        axios.spread((...responses) => {
          const responseOne = responses[0];
          const responseTwo = responses[1];
          const responesThree = responses[2];

          this.course = responseOne.data;
          this.myClass = responseTwo.data;
          this.trainers = responesThree.data.data;
          console.log(this.myClass);
        })
      )
      .catch((errors) => {
        // react on errors.
        console.log(errors);;
      });
  },
  methods: {
    async assignTrainer(event) {
      event.preventDefault();

      const apiUrl = "http://localhost:5002/assignTrainerClass";

      const trainerData = {
        classId: this.myClass.classId,
        trainerAssigned: this.selectedTrainer.userId,
        trainerName: this.selectedTrainer.userName,
      };

      try {
        let response = await axios.put(apiUrl, trainerData);
        console.log(response);
        if (response.status == 200) {
          this.data = response.data;
          this.error = false;
          this.message = "Trainer Successfully Assigned! 😃";
        } else {
          this.error = true;
          this.message = "Error! Please try again";
        }
      } catch (err) {
        console.log(err);
        this.error = true;
        this.message = err;
      }
    },
  },
};
</script>  

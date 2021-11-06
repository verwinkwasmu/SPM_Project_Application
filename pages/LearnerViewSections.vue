<template>
  <div id="App">
    <LearnerHeader />
    <Modal v-bind:message="message" />

    <main id="main">
      <div class="content">
        <section id="faq" class="faq section-bg">
          <div class="sidenav">
            <div v-for="n in totalNumSections + -1" :key="n">
              <a v-if="n <= sectionsCompleted + 1" @click="forceRouting(n)"
                >Section {{ n }}</a
              >
              <a v-else>Section {{ n }} <b>(LOCKED)</b></a>
              <br />
            </div>

            <div v-if="sectionsCompleted == totalNumSections - 1">
              <a>Final Quiz</a>
            </div>
            <div v-else>
              <a>Final Quiz <b>(LOCKED)</b></a>
            </div>
          </div>
          <div class="container" data-aos="fade-up">
            <div class="section-title">
              <h2>{{ courseName }}</h2>
              <h3>{{ sectionTitle }}</h3>
              <p></p>
            </div>

            <div class="faq-list">
              <ul>
                <li
                  data-aos="fade-up"
                  data-aos-delay="200"
                  v-for="file in file_list"
                  :key="file.filename"
                >
                  <a
                    data-bs-toggle="collapse"
                    :data-bs-target="'#' + file.betterFileId"
                    class="collapsed"
                    >{{ sectionTitle }}: {{ file.filename }}
                    <i class="bx bx-chevron-down icon-show"></i
                    ><i class="bx bx-chevron-up icon-close"></i
                  ></a>
                  <div
                    :id="file.betterFileId"
                    class="collapse"
                    data-bs-parent=".faq-list"
                  >
                    <div class="embed-responsive embed-responsive-16by9">
                      <iframe
                        :src="file.url"
                        width="100%"
                        height="500px"
                      ></iframe>
                    </div>
                    <br />
                    <button
                      v-if="file.completed != true"
                      type="button"
                      @click="setFileCompleted(file.fileId)"
                      class="btn btn-outline-success"
                    >
                      Mark as Complete
                    </button>
                    <button
                      v-else
                      type="button"
                      disabled
                      class="btn btn-outline-info"
                    >
                      COMPLETED! 😃
                    </button>
                  </div>
                </li>
              </ul>
            </div>
            <div class="form-group" id="takequiz" v-if="showQuiz & sectionsCompleted < sectionNum">
              <router-link
                :to="{
                  path: '/LearnerTakeQuiz',
                  query: {
                    classId: classId,
                    sectionId: sectionTitle,
                    courseName: courseName,
                  },
                }"
                type="button"
                class="btn btn-primary"
                >Take {{ sectionTitle }} Quiz</router-link
              >
            </div>
            <div
              class="form-group"
              id="takequiz"
              v-else-if="sectionsCompleted >= sectionNum"
            >
              <router-link
                :to="{
                  path: '/LearnerViewQuizExplanation',
                  query: {
                    classId: classId,
                    sectionId: sectionTitle,
                    courseName: courseName,
                  },
                }"
                type="button"
                class="btn btn-primary"
                disable
                >View {{ sectionTitle }} Quiz Attempt!</router-link
              >
            </div>
          </div>
        </section>
      </div>
    </main>
  </div>
</template>

<script>
import axios from "axios";

export default {
  data() {
    return {
      sectionTitle: this.$route.query.sectionName,
      sectionName: this.$route.query.sectionName.replace(" ", ""),
      sectionNum: '',
      className:
        this.$route.query.classId.split(" ")[1] +
        this.$route.query.classId.split(" ")[2],
      courseId: this.$route.query.classId.split(" ")[0],
      file_list: [],
      completedFileIdList: [],
      showQuiz: false,
      message: "",
      courseName: this.$route.query.courseName,
      totalNumSections: "",
      classId: this.$route.query.classId,
      sectionsCompleted: ""
    };
  },
  async created() {
    this.sectionNum = this.$route.query.sectionName.split(" ")[1]
    const apiUrl1 = `http://localhost:5050/getFiles?courseId=${this.courseId}&className=${this.className}&sectionName=${this.sectionName}`;
    const apiUrl2 = "http://localhost:5001/getCompletedFiles";
    const apiUrl3 = "http://localhost:5004/getEnrolmentDetails";
    const apiUrl2_data = {
      courseId: this.courseId,
      className: this.className,
      sectionName: this.sectionName,
      learnerId: localStorage.getItem("userId"),
    };
    const apiUrl3_data = {
      classId: this.classId,
      learnerId: localStorage.getItem("userId"),
    };
    try {
      let response1 = await axios.get(apiUrl1);
      let response2 = await axios.post(apiUrl2, apiUrl2_data);
      let response3 = await axios.post(apiUrl3, apiUrl3_data);
      this.file_list = response1.data;
      this.completedFileIdList = response2.data;
      this.totalNumSections = parseInt(response3.data.totalNumSections);
      this.sectionsCompleted = response3.data.sectionsCompleted;

      const file_list = this.file_list;
      const completedFileIdList = this.completedFileIdList.data;

      file_list.forEach((element) => {
        if (completedFileIdList.includes(element.fileId)) {
          element.completed = true;
        }
      });
      console.log(this.file_list);
      if (this.completedFileIdList.data.length == this.file_list.length) {
        this.showQuiz = true;
      }
    } catch (err) {
      console.log(err);
    }
  },
  methods: {
    async setFileCompleted(fileId) {
      const apiUrl = "http://localhost:5001/setFileCompleted";
      const post_data = {
        learnerId: localStorage.getItem("userId"),
        fileId: fileId,
      };

      try {
        let response = await axios.post(apiUrl, post_data);
        if (response.status == 201) {
          this.message = "learning material completed!";
          this.$bvModal.show("bv-modal-example");
          setTimeout(
            function () {
              window.location.reload();
            }.bind(this),
            2000
          );
        } else {
          alert("Please try again!");
        }
      } catch (err) {
        console.log(err);
      }
    },
    forceRouting(n) {
      let section = "Section " + n;
      let link = `/LearnerViewSections?classId=${this.$route.query.classId}&courseName=${this.courseName}&sectionName=${section}`;
      window.location.replace(link);
    },
  },
};
</script>


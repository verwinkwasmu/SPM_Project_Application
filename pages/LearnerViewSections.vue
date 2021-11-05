<template>
  <div id="App">
    <LearnerHeader />
    <Modal v-bind:message="message" />

    <main id="main">
      <div class="content">
        <section id="faq" class="faq section-bg">
          <div class="sidenav">
            <a href="#">{{ sectionTitle }}</a>
            <a href="#" class="disabled">Section 2</a>
            <a href="#" class="disabled"> Section 3</a>
            <a href="#" class="disabled">Section 4</a>
          </div>
          <div class="container" data-aos="fade-up">
            <div class="section-title">
              <h2>{{ courseName }}</h2>
              <h3>{{ sectionName }}</h3>
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
                    >Section 1: {{ file.filename }}
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
            <div class="form-group" id="takequiz" v-if="showQuiz">
              <button type="button" class="btn btn-primary">Take Quiz</button>
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
  data: () => ({
    courseName: "Fundamentals of XXX",
    // this.$route.query.courseName,
    sectionTitle: "Section 1",
    sectionName: "Section1",
    // this.$route.query.sectionId.replace(" ", ""),
    className: "Class2",
    // this.$route.query.classTitle.replace(" ", ""),
    courseId: localStorage.getItem("courseId"),
    file_list: [],
    completedFileIdList: [],
    showQuiz: false,
    message: ""
  }),
  async created() {
    const apiUrl1 = `http://localhost:5050/getFiles?courseId=${this.courseId}&className=${this.className}&sectionName=${this.sectionName}`;
    const apiUrl2 = "http://localhost:5001/getCompletedFiles";

    const post_data = {
      courseId: this.courseId,
      className: this.className,
      sectionName: this.sectionName,
      learnerId: localStorage.getItem("userId"),
    };

    try {
      let response1 = await axios.get(apiUrl1);
      let response2 = await axios.post(apiUrl2, post_data);
      this.file_list = response1.data;
      this.completedFileIdList = response2.data;

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
  },
};
</script>


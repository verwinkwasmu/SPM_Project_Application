<template>
  <div>
    <TrainerHeader />
    <Modal :message="message" />
    <section id="team" class="team section-bg">
      <div class="container" data-aos="fade-up">
        <div class="row pb-5 mb-2 ml-0">
          <div class="viewClass">
            <router-link
              :to="{
                path: '/TrainerViewSection/',
                query: { classId: this.$route.query.classId },
              }"
              class="btn btn-primary"
              >Back to see all Sections</router-link
            >
          </div>
        </div>
        <div class="section-title">
          <h2>Fundamentals of Xerox WorkCentre 7845</h2>

          <div>
            <div class="mb-3">
              <label for="file" class="form-label">Upload File</label>
              <input
                class="form-control"
                type="file"
                id="file"
                ref="file"
                v-on:change="handleFileUpload()"
              />
            </div>
            <button class="btn btn-primary" @click="uploadFile()">
              Upload File
            </button>
          </div>
          <br />
          <div
            v-if="error == true"
            class="alert alert-danger mt-5"
            role="alert"
          >
            {{ message }}
          </div>
          <div
            v-else-if="error == false"
            class="alert alert-success"
            role="alert"
          >
            {{ message }}
          </div>
        </div>

        <table class="table">
          <thead>
            <tr>
              <th scope="col">File Name</th>
              <th scope="col">File Url</th>
              <th scope="col"></th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="file in file_list" :key="file.filename">
              <td>{{ file.filename }}</td>
              <td>
                <a>{{ file.url }}</a>
              </td>
              <td>
                <a
                  type="button"
                  class="btn btn-outline-danger"
                  @click="removeFile(file.filename)"
                  >Remove</a
                >
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
  data() {
    return {
      file: "",
      courseId: localStorage.getItem("courseId"),
      className: this.$route.query.classTitle.replace(" ", ""),
      sectionName: this.$route.query.sectionId.replace(" ", ""),
      file_list: [],
      error: null,
      message: "",
    };
  },
  async mounted() {
    this.error = null;

    const apiUrl = `https://spm-flask.herokuapp.com/getFiles?courseId=${this.courseId}&className=${this.className}&sectionName=${this.sectionName}`;

    try {
      let response = await axios.get(apiUrl);
      this.file_list = response.data;
    } catch (err) {
      console.log(err);
      // this.error = true;
      // this.message = err;
    }
  },
  methods: {
    async uploadFile() {
      this.error = null;
      const apiUrl = `https://spm-flask.herokuapp.com/upload?courseId=${this.courseId}&className=${this.className}&sectionName=${this.sectionName}`;

      let formData = new FormData();
      formData.append("file", this.file);

      try {
        let response = await axios.put(apiUrl, formData);
        if (response.status == 200) {
          this.error = false;
          this.message = "File Successfully Uploaded 😃 Reloading Page!";
          setTimeout(
            function () {
              window.location.reload();
            }.bind(this),
            2000
          );
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
    handleFileUpload() {
      this.file = this.$refs.file.files[0];
    },
    async removeFile(filename) {
      const apiUrl = "https://spm-flask.herokuapp.com/removeFile";

      const file_data = {
        courseId: this.courseId,
        className: this.className,
        sectionName: this.sectionName,
        fileName: filename,
      };

      try {
        let response = await axios.delete(apiUrl, { data: file_data });
        if (response.status == 200) {
          this.message = "File removed successfully 😇 Reloading Page!";
          this.$bvModal.show("bv-modal-example");
          setTimeout(
            function () {
              window.location.reload();
            }.bind(this),
            2000
          );
        } else {
          alert("Please Try again!");
        }
      } catch (err) {
        console.log(err);
      }
    },
  },
};
</script>

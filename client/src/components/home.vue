<template>
  <b-container fluid>
    <!-- COMPONENTS -->

    <b-row class="mt-4">
      <b-col>
        <picture-input
          class="mt-3"
          ref="pictureInput"
          @change="onChanged"
          @remove="onRemoved"
          :width="500"
          :removable="true"
          removeButtonClass="btn"
          :height="500"
          accept="image/jpeg, image/png, image/gif"
          buttonClass="ui btn primary"
          :customStrings="{
            upload: '<h1>Upload it!</h1>',
            drag: 'Drag and drop your image here'
          }"
        ></picture-input>
        <b-button
          class="btn"
          variant="outline-dark"
          @click="attemptUpload"
          v-if="imageup"
          v-bind:class="{ disabled: !image }"
        >Upload</b-button>
      </b-col>
      <b-col>
        <div class="m-3">
          <h3 class="mb-3">Recognised text</h3>
          {{ ocrtext }}
        </div>
      </b-col>
    </b-row>
  </b-container>
</template>

<script>
/* eslint-disable */
import axios from "axios";
export default {
  sockets: {
    connect: function() {
      this.$socket.emit("connected_event", {
        data: "WebSocket has been connected successfully."
      });
    },
    text_response: function(msg) {
      this.ocrtext = msg.data;
    }
  },
  data() {
    return {
      imageup: false,
      image: "",
      ocrtext: ""
    };
  },
  methods: {
    onChanged(e) {
      if (this.$refs.pictureInput.file) {
        console.log("New picture loaded");
        this.image = this.$refs.pictureInput.file;
        this.imageup = true;
      } else {
        console.log("Old browser. No support for Filereader API");
      }
    },
    onRemoved() {
      this.image = "";
      this.ocrtext = "";
    },
    attemptUpload() {
      if (this.image) {
        const formData = new FormData();
        formData.append("file", this.image);
        this.$Progress.start();
        axios
          .post("http://127.0.0.1:5000/file-upload", formData)
          .then(response => {
            this.$Progress.finish();
            if (response.data.success) {
              this.image = "";
              console.log("Image uploaded successfully ✨");
            }
          })
          .catch(err => {
            console.error("Axios post error");
            this.$Progress.finish();
          });
      }
    }
  }
};
</script>



<style scoped>
.custom-card,
.btn {
  border-radius: 15px;
  border-style: solid;
  border-color: #333a40;
}
</style>

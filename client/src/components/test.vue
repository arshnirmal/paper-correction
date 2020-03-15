<template>
  <b-container fluid>
    <!-- COMPONENTS -->

    <b-row>
      <b-col>
        <b-form-file
          class="mt-3"
          v-model="filetxt"
          :state="Boolean(file)"
          placeholder="Choose a file for better autocorrection.."
          size="sm"
          drop-placeholder="Drop file here..."
        ></b-form-file>

        <picture-input
          class="mt-3"
          ref="pictureInput"
          @change="onChanged"
          @remove="onRemoved"
          :width="500"
          :removable="true"
          removeButtonClass="ui red btn"
          :height="500"
          accept="image/*, application/pdf"
          buttonClass="ui btn primary"
          :customStrings="{
            upload: '<h1>Upload it!</h1>',
            drag: 'Drag and drop your image here'
          }"
        ></picture-input>
        <b-button
          variant="outline-dark"
          @click="attemptUpload"
          v-if="imageup"
          v-bind:class="{ disabled: !image }"
          >Upload</b-button
        >
      </b-col>
      <b-col>
        <div class="m-3">
          <h3 class="mb-3">
            Recognised text
          </h3>
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
       console.log("connected");
    },
    text_response: function(msg) {
      this.ocrtext = msg.data
   }
  },
  data() {
    return {
      filetxt:null,
      imageup: false,
      clientMsg: "",
      ocrtext: "",
      file:"",
    
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
    },
    attemptUpload() {
      if (this.image) {
        const formData = new FormData();
        formData.append("file", this.filetxt);
        formData.append("file", this.image);
        // formData.append("textfile", this.form.filetxt);
        axios
          .post("http://127.0.0.1:5000/file-upload", formData)
          .then(response => {
            this.image = "";
            console.log("Image uploaded successfully ✨")
          })
          .catch(err => {
            console.error("Axios post error");
          });

      }
    }
    }
};
</script>

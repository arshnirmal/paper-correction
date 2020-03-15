<template>
  <b-container fluid>
    <b-row>
      <b-col>
        <div class="studentarea">
          <b-row>
            <h5>
              Please add the papers to be corrected
              <input
                type="file"
                id="files"
                ref="files"
                multiple
                v-on:change="handleFilesUpload()"
              />
            </h5>
          </b-row>
          <b-row>
            <div class="filesection">
              <div v-for="(file, key) in files" class="file-listing" v-bind:key="key">
                {{ file.name }}
                <span class="remove-file" v-on:click="removeFile(key)">Remove</span>
              </div>
            </div>
          </b-row>

          <b-row>
            <b-col>
              <b-button class="pb-2 m-2" variant="primary" v-on:click="addFiles()"
                >Add Files</b-button
              >
            </b-col>

            <b-col>
              <b-button class="pb-2 m-2" variant="success" v-on:click="submitFiles()"
                >Submit</b-button
              >
            </b-col>
          </b-row>
        </div>
      </b-col>
      <!-- Master copy -->
      <b-col class="studentarea">
        <b-row>
          <b-form-file
            class="m-3 solo"
            v-model="filetxt"
            :state="Boolean(file)"
            placeholder="Choose a file for better autocorrection.."
            size="sm"
            drop-placeholder="Drop file here..."
          ></b-form-file>
        </b-row>
        <b-row>
          <b-form-file
            class="m-3"
            v-model="filetxt"
            :state="Boolean(file)"
            placeholder="Please add master copy"
            size="sm"
            drop-placeholder="Drop file here..."
          ></b-form-file>
        </b-row>
      </b-col>
    </b-row>
  </b-container>
</template>

<script>
/* eslint-disable */
import axios from "axios";
export default {
  /*
      Defines the data used by the component
    */
  data() {
    return {
      files: []
    };
  },

  /*
      Defines the method used by the component
    */
  methods: {
    /*
        Adds a file
      */
    addFiles() {
      this.$refs.files.click();
    },

    /*
        Submits files to the server
      */
    submitFiles() {
      /*
          Initialize the form data
        */
      let formData = new FormData();

      /*
          Iteate over any file sent over appending the files
          to the form data.
        */
      for (var i = 0; i < this.files.length; i++) {
        let file = this.files[i];

        formData.append("file", file);
      }

      /*
          Make the request to the POST /select-files URL
        */
      console.log(files.length);
      axios
        .post("http://127.0.0.1:5000/file-upload", formData)
        .then(response => {
          console.log("Files have been uploaded");
        })
        .catch(err => {
          console.error("Axios post error");
        });
    },

    /*
        Handles the uploading of files
      */
    handleFilesUpload() {
      let uploadedFiles = this.$refs.files.files;

      /*
          Adds the uploaded file to the files array
        */
      for (var i = 0; i < uploadedFiles.length; i++) {
        this.files.push(uploadedFiles[i]);
      }
    },

    /*
        Removes a select file the user has uploaded
      */
    removeFile(key) {
      this.files.splice(key, 1);
    }
  }
};
</script>
<style>
input[type="file"] {
  position: absolute;
  top: -500px;
}

div.file-listing {
  width: 200px;
}

span.remove-file {
  color: red;
  cursor: pointer;
  float: right;
}
.studentarea {
  background: #f0e8e6;
  border-radius: 6px;
  position: relative;
}
.solo {
  background: #f0e8e6;
}
h5 {
  margin: auto;
  padding-top: 5px;
}
</style>
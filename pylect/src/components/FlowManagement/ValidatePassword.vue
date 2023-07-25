<template>
    <Modal v-model="showModal" width="30%" @on-cancel="handleCancel">
        <p slot="header" style="color:#f60;text-align:center">
            <Icon type="information-circled"></Icon>
            <span>Check Password</span>
        </p>
        <Form ref="formCustom" :model="formCustom" :rules="ruleCustom" :label-width="80">
            <FormItem label="密码" prop="oldPasswd">
                <Input type="password" v-model="formCustom.oldPasswd" placeholder="输入密码"></Input>
            </FormItem>
        </Form>
        <div slot="footer">
            <Button type="primary" @click="handleSubmit('formCustom')">Submit</Button>
            <Button @click="handleCancel">Cancel</Button>
        </div>
    </Modal>
  </template>
  
  <script>
  
  function pyCheckPassowrd(params, callback){
    pywebview.api.checkPassword(JSON.stringify(params)).then(res => {          
      if (null != callback){
        console.log('pyCheckPassowrd response:', res);
        callback(res)
      }
    })
  }
  
  export default {
    props: ["show"],
    data() {
      const validateOldPasswd = (rule, value, callback) => {
        let params = {
          password: value,
        };
        pywebview.api.checkPassword(JSON.stringify(params)).then((res) => {
          if (res.code !== 200) {
            callback(new Error("密码错误"));
          } else {
            callback();
          }
        });
      };
  
      return {
        showModal: this.show,
        formCustom: {
          oldPasswd: "",
        },
        ruleCustom: {
          oldPasswd: [
            { validator: validateOldPasswd, trigger: "blur" },
          ],
        },
      };
    },
    watch: {
      show(val) {
        this.showModal = val;
      },
    },
    methods: {
      handleSubmit(name) {
        this.$refs[name].validate((valid) => {
          if (valid) {
            let params = {
              password: this.formCustom.oldPasswd,
            };
  
            pyCheckPassowrd(params, (res) => {
              if (res.code === 200) {
                this.$Message.success("密码正确!");
                this.$emit('passwordCorrect'); 
                this.handleCancel();
              } else {
                this.$Message.error("密码错误!");
              }
            })
          } else {
            this.$Message.error("表单验证失败!");
          }
        });
      },
      handleCancel() {
        this.$refs.formCustom.resetFields();
        this.showModal = false;
        this.$emit("update:show", false);
      },
    },
  };
  </script>
  
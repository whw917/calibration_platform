<template>
    <Form ref="formCustom" :model="formCustom" :rules="ruleCustom" :label-width="80">
      <FormItem label="旧密码" prop="oldPasswd">
        <Input type="password" v-model="formCustom.oldPasswd"></Input>
      </FormItem>
      <FormItem label="新密码" prop="passwd">
        <Input type="password" v-model="formCustom.passwd"></Input>
      </FormItem>
      <FormItem label="确认密码" prop="passwdCheck">
        <Input type="password" v-model="formCustom.passwdCheck"></Input>
      </FormItem>
  
      <FormItem>
        <Button type="primary" @click="handleSubmit('formCustom')">提交</Button>
        <Button @click="handleReset('formCustom')" style="margin-left: 8px">重置</Button>
      </FormItem>
    </Form>
  </template>
  
  <script>
  
  
  //---------------------
  /** 
  * 
  * @param {*} params: {
  *                     "password": "123123"
  *                    } 
  * @param {*} callback 回调
  */
  function pyCheckPassowrd(params, callback){
  pywebview.api.checkPassword(JSON.stringify(params)).then(res => {          
    if (null != callback){
      console.log('pyCheckPassowrd response:', res);
      callback(res)
    }
  })
  }
  
  
  /**
  * 
  * @param {*} params: {
  *                     "oldPassword": "123123",
  *                     "newPpassword": "aabbcc"
  *                    } 
  * @param {*} callback 回调
  */
  function pySetPassowrd(params, callback){
  pywebview.api.setPassword(JSON.stringify(params)).then(res => {          
    if (null != callback){
      console.log('pySetPassowrd response:', res);
      callback(res)
    }
  })
  }
  
  
  export default {
    data() {
      const validatePass = (rule, value, callback) => {
        if (value === '') {
          callback(new Error('请输入密码'));
        } else {
          callback();
        }
      };
      const validatePassCheck = (rule, value, callback) => {
        if (value === '') {
          callback(new Error('请在此输入密码'));
        } else if (value !== this.formCustom.passwd) {
          callback(new Error('两次输入的密码不同'));
        } else {
          callback();
        }
      };
      return {
        formCustom: {
          oldPasswd: '',
          passwd: '',
          passwdCheck: '',
        },
        ruleCustom: {
          oldPasswd: [
            { validator: validatePass, trigger: 'blur' },
          ],
          passwd: [
            { validator: validatePass, trigger: 'blur' },
          ],
          passwdCheck: [
            { validator: validatePassCheck, trigger: 'blur' },
          ],
        },
      };
    },
    methods: {
      handleSubmit(name) {
        this.$refs[name].validate((valid) => {
          if (valid) {
            let paramsA = {
              password: this.formCustom.oldPasswd,
            };
            pywebview.api.checkPassword(JSON.stringify(paramsA)).then((res) => {
              if (res.code === 200) {
                let paramsB = {
                  oldPassword: this.formCustom.oldPasswd,
                  newPassword: this.formCustom.passwd,
                };
                pywebview.api.setPassword(JSON.stringify(paramsB)).then((res) => {
                  if (res.code === 200) {
                    this.$Message.success('密码更新成功!');
                  } else {
                    this.$Message.error('密码更新失败!');
                  }
                });
              } else {
                this.$Message.error('旧密码错误!');
              }
            });
          } else {
            this.$Message.error('表单验证失败!');
          }
        });
      },
      handleReset(name) {
        this.$refs[name].resetFields();
      },
    },
  };

  </script>
  
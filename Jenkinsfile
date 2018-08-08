#!/usr/bin/env groovy

properties([
  parameters([
    string(name: 'DEPLOY_ENV1', defaultValue: 'TESTING1', description: 'The target environment1', ),
    string(name: 'DEPLOY_ENV2', defaultValue: 'TESTING2', description: 'The target environment2', ),
//    booleanParam(defaultValue: true, description: '', name: 'userFlag'),
//    choice(choices: 'kalyan\nsrikanth', description: 'Which Son?', name: 'son'),
//    password(name: 'ENV_PASSWORD', defaultValue: '', description: 'Enter password!'),
   ])
])

echo env.DEPLOY_ENV1

node {
  dir('camunda_common') {
//		git branch: 'release/18.08', 
//			credentialsId: 'vp2592', 
//			url: 'https://codecloud.web.att.com/scm/st_oce/camunda_common.git'
    }
  dir('camunda_entertainment_group') {
//		git branch: 'release/1808', 
//			credentialsId: 'vp2592', 
//			url: 'https://codecloud.web.att.com/scm/st_oce/camunda_entertainment_group.git'
    }
  dir('oce_framework') {
//		git branch: 'release/18.08', 
//			credentialsId: 'vp2592', 
//			url: 'https://codecloud.web.att.com/scm/st_oce/oce_framework.git'
    }
}

pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                echo 'Building..'
         //       sh 'mvn -f initial/pom.xml clean compile'
            }
        }
        stage('Test') {
            steps {
                echo 'Testing..'
        //        sh 'mvn -f initial/pom.xml clean test'
            }
        }
        stage('CodeCoverage') {
            steps {
                echo 'Code Coveraging....'
            }
        }
        stage('CodeAnalysis') {
            steps {
                echo 'Code Analyzing....'
             //   sh 'mvn sonar:sonar -f initial/pom.xml -Dsonar.host.url=http://localhost:9000 -Dsonar.login=7d69663e1b687e7dcce539aa3c18c2b72312a91b'
            }
        }
        stage('CodePackaging') {
            steps {
                echo 'Code Packaging....'
          //      sh 'mvn -f initial/pom.xml clean package'
            }
        }
        stage('DeployToDev') {
            steps {
                echo 'Deploying to Dev server....'
            }
        }
    }
}

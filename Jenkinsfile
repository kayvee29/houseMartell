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
  dir('Lannister') {
        git url: 'https://github.com/kayvee29/houseLannister.git'
    }
  dir('ajsc5') {
        git url: 'https://github.com/kayvee29/ajsc5.git'
    }
  dir('stark') {
        git url: 'https://github.com/kayvee29/house-stark.git'
    }
}

pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                echo 'Building..'
            }
        }
        stage('Test') {
            steps {
                echo 'Testing..'
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
            }
        }
        stage('CodePackaging') {
            steps {
                echo 'Code Packaging....'
            }
        }
        stage('DeployToDev') {
            steps {
                echo 'Deploying to Dev server....'
            }
        }
    }
}

# -*- coding: utf-8 -*-

import os
import sys
import torch

from arizona.nlu.models.jointbert_nlu import JointBERTNLU

class JointBERTNLULearner():
    def __init__(
        self,
        model: JointBERTNLU=None,
        device: str=None
    ) -> None:
        super(JointBERTNLULearner, self).__init__()

        self.model = model

        if not device:
            self.device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
        else:
            self.device = device

    def train(
        self,
        **kwargs
    ):
        raise NotImplementedError

    def evaluate(
        self, 
        view_report: bool=True,
        **kwargs
    ):
        raise NotImplementedError

    def inference(
        self,
        input: str=None,
        **kwargs
    ):
        raise NotImplementedError

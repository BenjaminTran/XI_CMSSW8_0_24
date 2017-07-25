import FWCore.ParameterSet.Config as cms

xiTree = cms.EDAnalyzer('XiOmTTree',
     vertexCollName  = cms.InputTag('offlinePrimaryVertices'),
     v0CollName      = cms.string('generalCascadeCandidatesNew'),
     #v0CollName      = cms.string('generalV0CandidatesNew'),
     v0IDName = cms.string('Xi')
)
